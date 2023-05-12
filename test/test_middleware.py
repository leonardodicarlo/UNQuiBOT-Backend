import unittest

from interface.impl.interfazSQL import InterfazMySQL
from interface.interfazTemplate import InterfazTemplate
from interface.middleware import Middleware
from persistence.carreraDAO import CarrerasDAO
from test.db.dbTesting import DatabaseMemory


class MiddlewareTest(unittest.TestCase):

    def setUp(self):
        """ elementos para testing """
        daoTest: CarrerasDAO = CarrerasDAO(DatabaseMemory())
        interfaceSQL: InterfazTemplate = InterfazMySQL(daoTest)
        self.middlewareTest = Middleware(interfaceSQL)

        # # prueba select
        # select = self.middlewareTest.infoMateriasPorCarrera(1)

    def test_cant_materias_tpi(self):
        idMateria = int(1)

        response = self.middlewareTest.cantidadMateriasPorCarrera(idMateria)
        expected = "La carrera Tecnicatura en Programacion Informatica tiene 34 materias"
        self.assertEqual(response, expected)
    
    def test_materias_tpi(self):
        idMateria = int(1)

        response = self.middlewareTest.infoMateriasPorCarrera(idMateria)
        expected = "Las materias de la carrera Tecnicatura en Programacion Informatica son: <br/> -Bases de Datos<br/> -Bases de Datos II<br/> -Construccion de Interfaces de Usuario<br/> -Derechos de Autor y Derechos de Copia en la Era Digital<br/> -Desarrollo de Aplicaciones<br/> -Elementos de Ingenieria de Software<br/> -Elementos de programacion y logica<br/> -Estrategias de Persistencia<br/> -Estructuras de Datos<br/> -Herramientas Declarativas en Programacion<br/> -Introduccion a la Bioinformatica<br/> -Introduccion a la Programacion<br/> -Introduccion a las Arquitecturas de Software<br/> -Introduccion al Desarrollo de Videojuegos<br/> -Laboratorio de Sistemas Operativos y Redes<br/> -Lectura y Escritura Academica<br/> -Matematica<br/> -Matematica I<br/> -Matematica II<br/> -Organizacion de Computadoras<br/> -Participacion y Gestion en Proyectos de Software Libre<br/> -Politicas Publicas en la Sociedad de la Informacion y la Era Digital<br/> -Programacion con Objetos I<br/> -Programacion con Objetos II<br/> -Programacion con Objetos III<br/> -Programacion Concurrente<br/> -Programacion Funcional<br/> -Redes de Computadoras<br/> -Seguridad de la Informacion<br/> -Seminarios<br/> -Seminarios sobre Herramientas o Tecnicas Puntuales<br/> -Sistemas de Informacion Geografica<br/> -Sistemas Operativos<br/> -Trabajo de Insercion Profesional"
        self.assertEqual(response, expected)

if __name__ == '__main__':
    unittest.main()

