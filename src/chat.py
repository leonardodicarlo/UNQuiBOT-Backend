import random
import json
import torch
import os

# Obtiene la ruta absoluta del directorio que contiene el script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Combina la ruta absoluta del directorio del script con la ruta relativa al archivo
intents_file = os.path.join(script_dir, 'intents.json')
data_file = os.path.join(script_dir, 'data.pth')

from src.model import NeuralNet
from src.nltk_utils import bag_of_words, tokenize
from interface.middleware import Middleware


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open(intents_file, 'r') as json_data:
    intents = json.load(json_data)

data = torch.load(data_file)

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
interface = Middleware()


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
    if prob.item() > 0.99:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                if "info materias - " in tag:
                    return interface.infoMateriasPorCarrera(intent["value"])
                if "cantidad materias - " in tag:
                    return interface.cantidadMateriasPorCarrera(intent["value"])
                return random.choice(intent['responses'])
    return "No te entendí, todavía estoy aprendiendo..."


if __name__ == "__main__":
    print("Hablemos! (escribí 'salir' para finalizar)")
    while True:
        sentence = input("Vos: ")
        if sentence == "salir":
            break

        resp = get_response(sentence)