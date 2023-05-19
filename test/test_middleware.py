import unittest

from interface.middleware import Middleware
from test.db.dbTesting import DatabaseMemory


class MiddlewareTest(unittest.TestCase):

    def setUp(self):
        """ elementos para testing """
        self.dbTesting = DatabaseMemory()
        self.middlewareTest = Middleware()
        self.middlewareTest.currentInterface.dao.db = self.dbTesting
        self.middlewareTest.currentInterface.daoUser.db = self.dbTesting

    def test_cant_materias_con_carrera_SIN_materias_cargadas(self):
        """
        Se testea cargando en DB carrera sin materias relacionadas.
        """
        idCarreraTPI = 1

        # Carga de datos
        insertCarrera = "INSERT INTO carrera(id, nombre, depto) VALUES (" + str(
            idCarreraTPI) + ", 'Tecnicatura en Programacion Informatica', 'CYT');"
        self.dbTesting.ejecutarComandosMult(insertCarrera)

        # Test de metodo 'cantidadMateriasPorCarrera'
        response = self.middlewareTest.cantidadMateriasPorCarrera(idCarreraTPI)
        expected = "La carrera Tecnicatura en Programacion Informatica tiene 0 materias"
        self.assertEqual(response, expected)

    def test_cant_materias_con_carrera_2_materias_cargadas(self):
        """
        Se testea cargando en DB carrera y dos materias relacionadas.
        """
        idCarreraTPI = 1
        # Carga de datos
        insertCarreras = "INSERT INTO carrera(id, nombre, depto) VALUES (" + str(idCarreraTPI) + ", 'Tecnicatura en Programacion Informatica', 'CYT'),(2, 'Licenciatura en Informatica', 'CYT');"
        insertMaterias = "INSERT INTO materia (id,nombre) VALUES (165, 'Introduccion a la programacion'),(204,'Organizacion de Computadoras');"
        insertRelacionCarrera1 = "INSERT INTO carrera_materias (idCarrera,idMateria) VALUES (1, 165),(1, 204);"
        self.dbTesting.ejecutarComandosMult(insertCarreras + insertMaterias + insertRelacionCarrera1)

        # Test de metodo 'cantidadMateriasPorCarrera'
        response = self.middlewareTest.cantidadMateriasPorCarrera(idCarreraTPI)
        expected = "La carrera Tecnicatura en Programacion Informatica tiene 2 materias"
        self.assertEqual(response, expected)

    def test_info_materias_con_carrera_SIN_materias(self):
        """
        Se testea cargando en DB carrera y dos materias relacionadas.
        """
        idCarreraTPI = 1

        # Carga de datos
        insertCarreras = "INSERT INTO carrera(id, nombre, depto) VALUES (" + str(idCarreraTPI) + ", 'Tecnicatura en Programacion Informatica', 'CYT'),(2, 'Licenciatura en Informatica', 'CYT');"
        self.dbTesting.ejecutarComandosMult(insertCarreras)

        # Test de metodo 'infoMateriasPorCarrera'
        response = self.middlewareTest.infoMateriasPorCarrera(idCarreraTPI)
        expected = "Las materias de la carrera Tecnicatura en Programacion Informatica son: No existen materias cargadas."
        self.assertEqual(response, expected)

    def test_info_materias_con_carrera_2_materias(self):
        """
        Se testea cargando en DB carrera y dos materias relacionadas.
        """
        idCarreraTPI = 1

        # Carga de datos
        insertCarreras = "INSERT INTO carrera(id, nombre, depto) VALUES (" + str(idCarreraTPI) + ", 'Tecnicatura en Programacion Informatica', 'CYT'),(2, 'Licenciatura en Informatica', 'CYT');"
        insertMaterias = "INSERT INTO materia (id,nombre) VALUES (165, 'Introduccion a la programacion'),(204,'Organizacion de Computadoras');"
        insertRelacionCarrera1 = "INSERT INTO carrera_materias (idCarrera,idMateria) VALUES (1, 165),(1, 204);"
        self.dbTesting.ejecutarComandosMult(insertCarreras + insertMaterias + insertRelacionCarrera1)

        # Test de metodo 'infoMateriasPorCarrera'
        response = self.middlewareTest.infoMateriasPorCarrera(idCarreraTPI)
        expected = "Las materias de la carrera Tecnicatura en Programacion Informatica son: <br/> -Introduccion a la programacion<br/> -Organizacion de Computadoras"
        self.assertEqual(response, expected)

    def test_info_materias_con_carrera_NO_existente(self):
        idCarreraTPI = 1
        # No hay Carga de datos
        # Test de metodo 'infoMateriasPorCarrera' con id de Carrera no existente
        self.assertRaises(Exception, self.middlewareTest.infoMateriasPorCarrera, idCarreraTPI)

    def test_usuario_sin_materias_aprobadas(self):
        idUsuario = 1
        # Carga de datos
        insertUsuario = "INSERT INTO usuario(id, dni, legajo) VALUES (" + str(idUsuario) + ", 11222333, '1111');"
        self.dbTesting.ejecutarComandosMult(insertUsuario)

        # Test de metodo 'infoMateriasPorCarrera' con id de Carrera no existente
        response = self.middlewareTest.materiasAprobadasDelUsuario(idUsuario)
        expected = "Tenés las siguientes materias aprobadas: <br/>"
        self.assertEqual(response, expected)

    def test_usuario_con_2_materias_aprobadas(self):
        idUsuario = 1
        # Carga de datos
        insertUsuario = "INSERT INTO usuario(id, dni, legajo) VALUES (" + str(idUsuario) + ", 11222333, '1111');"
        insertMaterias = "INSERT INTO materia (id,nombre) VALUES (165, 'Introduccion a la programacion'),(204,'Organizacion de Computadoras');"
        insertUsuarioMateriasAprobadas = "INSERT INTO usuario_mcursadas (idUsuario,idMateria) VALUES("+str(idUsuario)+", 165),("+str(idUsuario)+", 204);"
        self.dbTesting.ejecutarComandosMult(insertUsuario+insertMaterias+insertUsuarioMateriasAprobadas)

        # Test de metodo 'materiasAprobadasDelUsuario'
        response = self.middlewareTest.materiasAprobadasDelUsuario(idUsuario)
        expected = "Tenés las siguientes materias aprobadas: <br/>Introduccion a la programacion <br/>Organizacion de Computadoras"
        self.assertEqual(response, expected)


if __name__ == '__main__':
    unittest.main()
