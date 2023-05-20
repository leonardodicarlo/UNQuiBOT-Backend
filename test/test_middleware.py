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
        self.middlewareTest.currentInterface.daoMateria.db = self.dbTesting

    def test_cant_materias_con_carrera_SIN_materias_cargadas(self):
        """
        test Cantidad de materias de carrera sin materias relacionadas.
        """
        idCarreraTPI = 1

        # Carga de datos
        insertCarrera = "INSERT INTO carrera(id, nombre, depto) VALUES (" + str(idCarreraTPI) + ", 'Tecnicatura en Programacion Informatica', 'CYT');"
        self.dbTesting.ejecutarComandosMult(insertCarrera)

        # Test de metodo 'cantidadMateriasPorCarrera'
        response = self.middlewareTest.cantidadMateriasPorCarrera(idCarreraTPI)
        expected = "La carrera Tecnicatura en Programacion Informatica tiene 0 materias"
        self.assertEqual(expected, response)

    def test_cant_materias_con_carrera_2_materias_cargadas(self):
        """
        test Cantidad de materias de carrera con Dos materias relacionadas.
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
        self.assertEqual(expected, response)

    def test_info_materias_con_carrera_SIN_materias(self):
        """
        test Info de materias de carrera sin materias relacionadas.
        """
        idCarreraTPI = 1

        # Carga de datos
        insertCarreras = "INSERT INTO carrera(id, nombre, depto) VALUES (" + str(idCarreraTPI) + ", 'Tecnicatura en Programacion Informatica', 'CYT'),(2, 'Licenciatura en Informatica', 'CYT');"
        self.dbTesting.ejecutarComandosMult(insertCarreras)

        # Test de metodo 'infoMateriasPorCarrera'
        response = self.middlewareTest.infoMateriasPorCarrera(idCarreraTPI)
        expected = "Las materias de la carrera Tecnicatura en Programacion Informatica son: No existen materias cargadas."
        self.assertEqual(expected, response)

    def test_info_materias_con_carrera_2_materias(self):
        """
        test Info de materias de carrera con Dos materias relacionadas.
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
        self.assertEqual(expected, response)

    def test_info_materias_con_carrera_NO_existente(self):
        """
        test Info de materias de carrera que no existe.
        """
        idCarreraTPI = 1
        # No hay Carga de datos
        # Test de metodo 'infoMateriasPorCarrera' con id de Carrera no existente
        self.assertRaises(Exception, self.middlewareTest.infoMateriasPorCarrera, idCarreraTPI)

    def test_usuario_sin_materias_aprobadas(self):
        """
        test Info de Materias Aprobadas de usuario que no cuenta con ninguna materia aprobada.
        """
        idUsuario = 1
        # Carga de datos
        insertUsuario = "INSERT INTO usuario(id, dni, legajo) VALUES (" + str(idUsuario) + ", 11222333, '1111');"
        self.dbTesting.ejecutarComandosMult(insertUsuario)

        # Test de metodo 'infoMateriasPorCarrera' con id de Carrera no existente
        response = self.middlewareTest.materiasAprobadasDelUsuario(idUsuario)
        expected = "Aún no tenés materias aprobadas"
        self.assertEqual(expected, response)

    def test_usuario_con_2_materias_aprobadas(self):
        """
        test Info de Materias Aprobadas de usuario que cuenta con DOS materias aprobadas.
        """
        idUsuario = 1
        # Carga de datos
        insertUsuario = "INSERT INTO usuario(id, dni, legajo) VALUES (" + str(idUsuario) + ", 11222333, '1111');"
        insertMaterias = "INSERT INTO materia (id,nombre) VALUES (165, 'Introduccion a la programacion'),(204,'Organizacion de Computadoras');"
        insertUsuarioMateriasAprobadas = "INSERT INTO usuario_mcursadas (idUsuario,idMateria,notaFinal) VALUES("+str(idUsuario)+", 165, 7),("+str(idUsuario)+", 204, 7);"
        self.dbTesting.ejecutarComandosMult(insertUsuario+insertMaterias+insertUsuarioMateriasAprobadas)

        # Test de metodo 'materiasAprobadasDelUsuario'
        response = self.middlewareTest.materiasAprobadasDelUsuario(idUsuario)
        expected = "Tenés las siguientes materias aprobadas: <br/>Introduccion a la programacion <br/>Organizacion de Computadoras"
        self.assertEqual(expected, response)

    def test_usuario_No_existente(self):
        """
        test Info de Materias Aprobadas de usuario que no existe.
        """
        idUsuario = 1
        # No hay Carga de datos

        # Test de metodo 'infoMateriasPorCarrera' con id de Carrera no existente
        response = self.middlewareTest.materiasAprobadasDelUsuario(idUsuario)
        expected = "Aún no tenés materias aprobadas"
        self.assertEqual(expected, response)

    def test_Promedio_de_usuario_sin_materias_aprobadas(self):
        """
        test Promedio de usuario que no cuenta con ninguna materia aprobada.
        """
        idUsuario = 1

        # Carga de datos
        insertUsuario = "INSERT INTO usuario(id, dni, legajo) VALUES (" + str(idUsuario) + ", 11222333, '1111');"
        self.dbTesting.ejecutarComandosMult(insertUsuario)

        # Test de metodo 'infoMateriasPorCarrera' con id de Carrera no existente
        response = self.middlewareTest.promedioDelUsuario(idUsuario)
        expected = "Aún no tenés notas cargadas"
        self.assertEqual(expected, response)

    def test_Promedio_de_usuario_con_2_materias_aprobadas(self):
        """
        test Promedio de usuario que cuenta con DOS materias aprobadas con Notas: 10 y 4, dando de promedio: 7.
        """
        idUsuario = 1
        nota1 = 10
        nota2 = 4

        # Carga de datos
        insertUsuario = "INSERT INTO usuario(id, dni, legajo) VALUES (" + str(idUsuario) + ", 11222333, '1111');"
        insertMaterias = "INSERT INTO materia (id,nombre) VALUES (165, 'Introduccion a la programacion'),(204,'Organizacion de Computadoras');"
        insertUsuarioMateriasAprobadas = "INSERT INTO usuario_mcursadas (idUsuario,idMateria, notaFinal) VALUES("+str(idUsuario)+", 165, "+str(nota1)+"),("+str(idUsuario)+", 204, "+str(nota2)+");"
        self.dbTesting.ejecutarComandosMult(insertUsuario + insertMaterias + insertUsuarioMateriasAprobadas)

        # Test de metodo 'infoMateriasPorCarrera' con id de Carrera no existente
        response = self.middlewareTest.promedioDelUsuario(idUsuario)
        expected = "Tu promedio actual es: 7.0"
        self.assertEqual(expected,response)

    def test_info_Cursada_actuales_de_Materia_Intro(self):
        """
        Test de informacion sobre Cursada segun idMateria, con Cursada y Materia existentes
        """
        idMateria = 166

        # Carga de datos
        insertMaterias = "INSERT INTO materia (id,nombre) VALUES ("+str(idMateria)+", 'Introduccion a la Programación');"
        insertCursadasIntro = "INSERT INTO cursada (id,idMateria,comision,nombreMateria,emailGrupo,horarios,periodo,activa,aulas) VALUES" \
                              "(1,"+str(idMateria)+",1,'Introducción a la Programación','tpi-est-inpr@listas.unq.edu.ar','Lun 09:00 a 11:59 - Mie 09:00 a 10:59(Virtual) - Jue 09:00 a 11:59','C12023',1,'37B - Virtual - 37B')," \
                              "(2,"+str(idMateria)+",2,'Introducción a la Programación','tpi-est-inpr@listas.unq.edu.ar','Lun 12:00 a 14:59 - Mie 09:00 a 10:59 - (Virtual) Jue 12:00 a 14:59','C12023',1,'37B - Virtual - 37B');"
        self.dbTesting.ejecutarComandosMult(insertMaterias+insertCursadasIntro)

        response = self.middlewareTest.infoMateria(idMateria)
        expected = "Materia: Introducción a la Programación\n<br/>Lista de Mail: tpi-est-inpr@listas.unq.edu.ar\n\n<br/>Horarios y Aulas:\nLun 09:00 a 11:59 - Mie 09:00 a 10:59(Virtual) - Jue 09:00 a 11:59 - 37B - Virtual - 37B\n<br/>Lun 12:00 a 14:59 - Mie 09:00 a 10:59 - (Virtual) Jue 12:00 a 14:59 - 37B - Virtual - 37B"
        self.assertEqual(expected, response)

    def test_info_Cursada_No_Existente_de_Materia_Intro(self):
        """
        Test de informacion sobre Cursada segun idMateria, con Cursada no existentes
        """
        idMateria = 166

        # Carga de datos
        insertMaterias = "INSERT INTO materia (id,nombre) VALUES ("+str(idMateria)+", 'Introduccion a la Programación');"
        self.dbTesting.ejecutarComandosMult(insertMaterias)

        response = self.middlewareTest.infoMateria(idMateria)
        expected = "No existen Cursadas activas para esa materia..."
        self.assertEqual(expected, response)

if __name__ == '__main__':
    unittest.main()
