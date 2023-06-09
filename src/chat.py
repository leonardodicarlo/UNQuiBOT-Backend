import random
import json
import torch
import os
import logging
import logstash

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

class Logging(object):
    def __init__(self, logger_name='python-logger',
                 log_stash_host='localhost',
                 log_stash_upd_port=5959

                 ):
        self.logger_name = logger_name
        self.log_stash_host = log_stash_host
        self.log_stash_upd_port = log_stash_upd_port


    def get(self):
        logging.basicConfig(
            filename="logfile",
            filemode="a",
            format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
            datefmt="%H:%M:%S",
            level=logging.INFO,
        )

        self.stderrLogger = logging.StreamHandler()
        logging.getLogger().addHandler(self.stderrLogger)
        self.logger = logging.getLogger(self.logger_name)
        self.logger.addHandler(logstash.LogstashHandler(self.log_stash_host,
                                                        self.log_stash_upd_port,
                                                        version=1))
        return self.logger

instance = Logging(log_stash_upd_port=5959, log_stash_host='localhost', logger_name='ChatLog')
logger = instance.get()

class IntentHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, intent, usr):
        raise NotImplementedError("Las subclases deben implementar este método")

    def set_next_handler(self, handler):
        self.next_handler = handler


class InfoCarrerasHandler(IntentHandler):
    def handle(self, intent, usr):
        if "info materias - " in intent["tag"]:
            return interface.infoMateriasPorCarrera(intent["value"])
        elif self.next_handler is not None:
            return self.next_handler.handle(intent, usr)


class CantidadMateriasHandler(IntentHandler):
    def handle(self, intent, usr):
        if "cantidad materias - " in intent["tag"]:
            return interface.cantidadMateriasPorCarrera(intent["value"])
        elif self.next_handler is not None:
            return self.next_handler.handle(intent, usr)

class InfoMateriasHandler(IntentHandler):
    def handle(self, intent, usr):
        if "info materia - " in intent["tag"]:
            return interface.infoMateria(intent["value"])
        elif self.next_handler is not None:
            return self.next_handler.handle(intent, usr)

class InfoUsuarioHandler(IntentHandler):
    def handle(self, intent, usr):
        if ("info usuario -" in intent["tag"]) and (usr == 0):
                return "Aún no estás logueado, no puedo responderte esa información."
        elif self.next_handler is not None:
            return self.next_handler.handle(intent, usr)

class InfoUsuarioCursadas(IntentHandler):
    def handle(self, intent, usr):
        if "Materias Cursadas" in intent["tag"]:
            return interface.materiasAprobadasDelUsuario(usr)
        elif self.next_handler is not None:
            return self.next_handler.handle(intent, usr)

class InfoUsuarioPromedio(IntentHandler):
    def handle(self, intent, usr):
        if "Promedio" in intent["tag"]:
            return interface.promedioDelUsuario(usr)
        elif self.next_handler is not None:
            return self.next_handler.handle(intent, usr)


class InfoUsuarioPosibles(IntentHandler):
    def handle(self, intent, usr):
        if "Posibles" in intent["tag"]:
            return interface.posiblesDelUsuario(usr)
        elif self.next_handler is not None:
            return self.next_handler.handle(intent, usr)

class DefaultHandler(IntentHandler):
    def handle(self, intent, usr):
        if intent["tag"] is not None:
            return random.choice(intent['responses'])
        return "No te entendí, todavía estoy aprendiendo..."


class IntentProcessor:
    def __init__(self):
        self.handlers = InfoCarrerasHandler(
            CantidadMateriasHandler(
                InfoMateriasHandler(
                    InfoUsuarioHandler(
                        InfoUsuarioCursadas(
                            InfoUsuarioPromedio(
                                InfoUsuarioPosibles(
                                    DefaultHandler()
                                )
                            )
                        )
                    )
                )
            )
        )

    def process(self, intent, usr):
        return self.handlers.handle(intent, usr)

def get_response(msg, usr):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    dict_log = {
    "tag": tag,
    "question": msg,
    "cookieUser": usr
    }

    json_log = json.dumps(dict_log)

    if prob.item() > 0.999:
        intent = None

        for i in intents['intents']:
            if i["tag"] == tag:
                intent = i
                logger.info(json_log)
                break
        if intent is not None:
            return IntentProcessor().process(intent, usr)
    dict_log['tag'] = "pregunta sin respuesta"
    logger.info(json.dumps(dict_log))
    return "No te entendí, todavía estoy aprendiendo..."

if __name__ == "__main__":
    print("Hablemos! (escribí 'salir' para finalizar)")
    while True:
        sentence = input("Vos: ")
        if sentence == "salir":
            break

        resp = get_response(sentence)
