import unittest
from src.chat import get_response

class ChatTest(unittest.TestCase):

    def setUp(self):
        pass

    bienvenida_responses = [ "Hola! :)", "Hola, ¿en qué te puedo ayudar?","Hola, Â¿en quÃ© te puedo ayudar?",
        "Buenas! ¿Qué puedo hacer por vos?", "¿Cómo estás?¿En qué te ayudo?",
        "Buenas! Â¿QuÃ© puedo hacer por vos?", "Â¿Cómo estÃ¡s?Â¿En quÃ© te ayudo?"
    ]
    despedida_responses = [ "Chau, gracias por tu visita!", "Hasta luego!", "Chau, gracias!"]
    agradecimiento_responses = ["Me alegra ayudarte!", "Perfecto, un placer", "Estoy a la orden!"]
    aulas_responses = [ "Aqui estan las aulas para este cuatrimestre: https://docs.google.com/spreadsheets/d/1dfhnJ2AH-tObDMXkmfNHLEfx7FnxGfE9/view#gid=1270991353", "AquÃ­ estÃ¡n las aulas para este cuatrimestre: https://docs.google.com/spreadsheets/d/1dfhnJ2AH-tObDMXkmfNHLEfx7FnxGfE9/view#gid=1270991353",
        "Este link del blog puede ayudarte http://cpi.blog.unq.edu.ar/aulas/"]

    def test_respuesta_bienvenida(self):
        msj_de_saludo = "Buenas"
        response = get_response(msj_de_saludo)
        print(response)
        self.assertTrue(response in self.bienvenida_responses)

    def test_respuesta_agradecimiento(self):
        msj_gracias = "Gracias, duda resuelta"
        response = get_response(msj_gracias)
        print(response)
        self.assertTrue(response in self.agradecimiento_responses)

    def test_respuesta_despedida(self):
        msj_adios = "Chau, nos vemos"
        response = get_response(msj_adios)
        print(response)
        self.assertTrue(response in self.despedida_responses)

    def test_respuesta_aulas_informacion(self):
        msj_aulas = "¿Cómo llego al aula?"
        response = get_response(msj_aulas)
        print(response)
        self.assertTrue(response in self.aulas_responses)


if __name__ == '__main__':
    unittest.main()
