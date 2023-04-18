import random
import json
import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

from persistence.carreraDAO import CarrerasDAO

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('./intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "./data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "UNQuiBOT"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.55:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                if "info materias - " in tag :
                    return infoMateriasPorCarrera(intent["value"])
                if "cantidad materias - " in tag :
                    return cantidadMateriasPorCarrera(intent["value"])
                return random.choice(intent['responses'])
    return "No te entendí, todavía estoy aprendiendo..."

# ---------------------- #
carrerasDAO = CarrerasDAO()
def infoMateriasPorCarrera(id):
    carrera = carrerasDAO.findCarreraById(id)
    infoCarrera= "Las materias de la carrera " + carrera.nombre + " son: " \
           + carrera.infoMaterias()
    return infoCarrera

def cantidadMateriasPorCarrera(id):
    carrera = carrerasDAO.findCarreraById(id)
    cantidadMaterias= "La carrera " + carrera.nombre + " tiene " \
           + str(len(carrera.materias)) + " materias"
    return cantidadMaterias


if __name__ == "__main__":
    print("Hablemos! (escribí 'salir' para finalizar)")
    while True:
        sentence = input("Vos: ")
        if sentence == "salir":
            break

        resp = get_response(sentence)
        print(resp)