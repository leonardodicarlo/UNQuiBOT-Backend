import unittest
import sys

sys.path.insert(0, '/Users/ldicarlo/Desktop/Documentos Míos/UnQ/TIP/UNQuiBOT-Backend/UNQuiBOT-Backend/')
##sys.path.insert(0, '/Users/ldicarlo/Desktop/Documentos Míos/UnQ/TIP/UNQuiBOT-Backend/')
##sys.path.insert(0,"/Users/ldicarlo/Library/Python/3.8/lib/python/site-packages")


from interface.middleware import Middleware


class MiddlewareTest(unittest.TestCase):
   
    def test_cant_materias_tpi(self):
        idMateria = int(1)
        middlewareTest = Middleware()
        response = middlewareTest.cantidadMateriasPorCarrera(idMateria)
        expected = "La carrera Tecnicatura en Programación Informática tiene 34 materias"
        self.assertEqual(response, expected)
    
    def test_materias_tpi(self):
        idMateria = int(1)
        middlewareTest = Middleware()
        response = middlewareTest.infoMateriasPorCarrera(idMateria)
        expected = "Las materias de la carrera Tecnicatura en Programación Informática son: <br/> -Bases de Datos<br/> -Bases de Datos II<br/> -Construcción de Interfaces de Usuario<br/> -Derechos de Autor y Derechos de Copia en la Era Digital<br/> -Desarrollo de Aplicaciones<br/> -Elementos de Ingeniería de Software<br/> -Elementos de programación y lógica<br/> -Estrategias de Persistencia<br/> -Estructuras de Datos<br/> -Herramientas Declarativas en Programación<br/> -Introducción a la Bioinformática<br/> -Introducción a la Programación<br/> -Introducción a las Arquitecturas de Software<br/> -Introducción al Desarrollo de Videojuegos<br/> -Laboratorio de Sistemas Operativos y Redes<br/> -Lectura y Escritura Académica<br/> -Matemática<br/> -Matemática I<br/> -Matemática II<br/> -Organización de Computadoras<br/> -Participación y Gestión en Proyectos de Software Libre<br/> -Políticas Públicas en la Sociedad de la Información y la Era Digital<br/> -Programación con Objetos I<br/> -Programación con Objetos II<br/> -Programación con Objetos III<br/> -Programación Concurrente<br/> -Programación Funcional<br/> -Redes de Computadoras<br/> -Seguridad de la Información<br/> -Seminarios<br/> -Seminarios sobre Herramientas o Técnicas Puntuales<br/> -Sistemas de Información Geográfica<br/> -Sistemas Operativos<br/> -Trabajo de Inserción Profesional"
        self.assertEqual(response, expected)

if __name__ == '__main__':
    unittest.main()

