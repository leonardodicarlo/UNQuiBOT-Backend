import unittest

from interface.middleware import Middleware
from test.db.dbTesting import DatabaseMemory
from test.db.insertsBuilder import InsertScriptBuilder


class MiddlewareTest(unittest.TestCase):

    def setUp(self):
        """ elementos para testing """
        self.dbTesting = DatabaseMemory()
        self.middlewareTest = Middleware()
        self.middlewareTest.currentInterface.dao.db = self.dbTesting
        self.middlewareTest.currentInterface.daoUser.db = self.dbTesting
        self.middlewareTest.currentInterface.daoMateria.db = self.dbTesting
        self.insertsBuilder = InsertScriptBuilder()

    def test_cant_materias_con_carrera_SIN_materias_cargadas(self):
        """
        test Cantidad de materias de carrera sin materias relacionadas.
        """
        idCarreraTPI = 1
        nombreTPI = "Tecnicatura en Programacion Informatica"

        # Carga de datos
        insertCarrera = self.insertsBuilder.carrera(idCarreraTPI, nombreTPI, "CYT")
        self.dbTesting.ejecutarComandosMult(insertCarrera)

        response = self.middlewareTest.cantidadMateriasPorCarrera(idCarreraTPI)
        expected = "tiene 0 materias"

        self.assertIn(expected, response)
        self.assertIn(nombreTPI, response)

    def test_cant_materias_con_carrera_2_materias_cargadas(self):
        """
        test Cantidad de materias de carrera con Dos materias relacionadas.
        """
        idCarreraTPI = 1
        # Carga de datos
        insertCarreras = self.insertsBuilder.carrera(idCarreraTPI, "Tecnicatura en Programacion Informatica", "CYT")
        insertMaterias = self.insertsBuilder.materia(1, 'Introduccion a la programacion', idCarreraTPI) + \
                         self.insertsBuilder.materia(2, 'Organizacion de Computadoras', idCarreraTPI)
        self.dbTesting.ejecutarComandosMult(insertCarreras + insertMaterias)

        response = self.middlewareTest.cantidadMateriasPorCarrera(idCarreraTPI)
        expected = "tiene 2 materias"
        self.assertIn(expected, response)

    def test_info_materias_con_carrera_SIN_materias(self):
        """
        test Info de materias de carrera sin materias relacionadas.
        """
        idCarreraTPI = 1
        # Carga de datos
        insertCarreras = self.insertsBuilder.carrera(idCarreraTPI, "Tecnicatura en Programacion Informatica", "CYT")
        self.dbTesting.ejecutarComandosMult(insertCarreras)

        response = self.middlewareTest.infoMateriasPorCarrera(idCarreraTPI)
        expected = "No existen materias cargadas."
        self.assertIn(expected, response)

    def test_info_materias_con_carrera_2_materias(self):
        """
        test Info de materias de carrera con Dos materias relacionadas.
        """
        idCarreraTPI = 1
        materia1Nombre = 'Introduccion a la programacion'
        materia2Nombre = 'Organizacion de Computadoras'

        # Carga de datos
        insertCarreras = self.insertsBuilder.carrera(idCarreraTPI, "Tecnicatura en Programacion Informatica", "CYT")
        insertMaterias = self.insertsBuilder.materia(1, materia1Nombre, idCarreraTPI) \
                         + self.insertsBuilder.materia(2, materia2Nombre, idCarreraTPI)
        self.dbTesting.ejecutarComandosMult(insertCarreras + insertMaterias)

        response = self.middlewareTest.infoMateriasPorCarrera(idCarreraTPI)
        self.assertIn(materia1Nombre, response)
        self.assertIn(materia2Nombre, response)

    def test_info_materias_con_carrera_NO_existente(self):
        """
        test Info de materias de carrera que no existe.
        """
        idCarreraTPI = 1
        # No hay Carga de datos

        self.assertRaises(Exception, self.middlewareTest.infoMateriasPorCarrera, idCarreraTPI)

    def test_usuario_sin_materias_aprobadas(self):
        """
        test Info de Materias Aprobadas de usuario que no cuenta con ninguna materia aprobada.
        """
        idUsuario = 1
        # Carga de datos
        insertUsuario = self.insertsBuilder.usuario(idUsuario, 123, "123")
        self.dbTesting.ejecutarComandosMult(insertUsuario)

        response = self.middlewareTest.materiasAprobadasDelUsuario(idUsuario)
        expected = "Aún no tenés materias aprobadas"
        self.assertEqual(expected, response)

    def test_usuario_con_2_materias_aprobadas(self):
        """
        test Info de Materias Aprobadas de usuario que cuenta con DOS materias aprobadas.
        """
        idUsuario = 1
        notaAprobado = 7
        materia1Nombre = 'Introduccion a la programacion'
        materia2Nombre = 'Organizacion de Computadoras'
        # Carga de datos
        insertUsuario = self.insertsBuilder.usuario(idUsuario, 123, "123")
        insertMaterias = self.insertsBuilder.materia(10, materia1Nombre, 1) + \
                         self.insertsBuilder.materia(11, materia2Nombre, 1)
        insertUsuarioMateriasAprobadas = self.insertsBuilder.usuarioxmateria(idUsuario, 10, notaAprobado) + \
                                         self.insertsBuilder.usuarioxmateria(idUsuario, 11, notaAprobado)
        self.dbTesting.ejecutarComandosMult(insertUsuario + insertMaterias + insertUsuarioMateriasAprobadas)

        response = self.middlewareTest.materiasAprobadasDelUsuario(idUsuario)
        self.assertIn(materia1Nombre, response)
        self.assertIn(materia2Nombre, response)

    def test_usuario_No_existente(self):
        """
        test Info de Materias Aprobadas de usuario que no existe.
        """
        idUsuario = 1
        # No hay Carga de datos

        response = self.middlewareTest.materiasAprobadasDelUsuario(idUsuario)
        expected = "Aún no tenés materias aprobadas"
        self.assertEqual(expected, response)

    def test_Promedio_de_usuario_sin_materias_aprobadas(self):
        """
        test Promedio de usuario que no cuenta con ninguna materia aprobada.
        """
        idUsuario = 1

        # Carga de datos
        insertUsuario = self.insertsBuilder.usuario(idUsuario, 123, "123")
        self.dbTesting.ejecutarComandosMult(insertUsuario)

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
        insertUsuario = self.insertsBuilder.usuario(idUsuario, 123, "123")
        insertMaterias = self.insertsBuilder.materia(10, 'Introduccion a la programacion', 1) + \
                         self.insertsBuilder.materia(11, 'Organizacion de Computadoras', 1)
        insertUsuarioMateriasAprobadas = self.insertsBuilder.usuarioxmateria(idUsuario, 10, nota1) + \
                                         self.insertsBuilder.usuarioxmateria(idUsuario, 11, nota2)
        self.dbTesting.ejecutarComandosMult(insertUsuario + insertMaterias + insertUsuarioMateriasAprobadas)

        response = self.middlewareTest.promedioDelUsuario(idUsuario)
        expected = str((nota1 + nota2) / 2)

        self.assertIn(expected, response)

    def test_Cursada_existente_se_retornan_sus_datos(self):
        """
        Test de informacion sobre Cursada segun idMateria, con Cursada y Materia existentes
        """
        idMateria = 166
        materiaNombre = 'Introduccion a la programacion'
        emailGrupo = 'tpi-est-inpr@listas.unq.edu.ar'
        hs1 = 'Lun 09:00 a 11:59 - Mie 09:00 a 10:59(Virtual) - Jue 09:00 a 11:59'
        aulas1 = '37B - Virtual - 37B'
        hs2 = 'Lun 12:00 a 14:59 - Mie 09:00 a 10:59 - (Virtual) Jue 12:00 a 14:59'
        aulas2 = '37B - Virtual - 60'

        # Carga de datos
        insertMaterias = self.insertsBuilder.materia(idMateria, materiaNombre, 1)
        insertCursadas = self.insertsBuilder.cursada(1, idMateria, 1, materiaNombre, emailGrupo, hs1, 'C12023', 1, aulas1) + \
                         self.insertsBuilder.cursada(2, idMateria, 2, materiaNombre, emailGrupo, hs2, 'C12023', 1, aulas2)
        self.dbTesting.ejecutarComandosMult(insertMaterias + insertCursadas)

        response = self.middlewareTest.infoMateria(idMateria)
        self.assertIn(materiaNombre, response)
        self.assertIn(emailGrupo, response)
        self.assertIn(hs1, response)
        self.assertIn(aulas1, response)
        self.assertIn(hs2, response)
        self.assertIn(aulas2, response)

    def test_Cursada_No_existente_no_retorna_informacion(self):
        """
        Test de informacion sobre Cursada segun idMateria, con Cursada no existentes
        """
        idMateria = 166

        # Carga de datos
        insertMaterias = self.insertsBuilder.materia(idMateria, 'Introduccion a la programacion', 1)
        self.dbTesting.ejecutarComandosMult(insertMaterias)

        response = self.middlewareTest.infoMateria(idMateria)
        expected = "No existen Cursadas activas para esa materia..."
        self.assertEqual(expected, response)

    def test_PosiblesMateriasParaUsuarioSinMateriasAprobadas(self):
        """
        Test materias posibles para un usuario sin materias aprobadas no puede inscribirse en materia con correlativa
        """
        idUsuario = 1
        materiaN1 = 'Elementos de programación y lógica'
        materia_ConCorrelativa = 'Introduccion a la programacion'

        # Carga de datos
        insertCarreras = self.insertsBuilder.carrera(1, "Tecnicatura en Programacion Informatica", "CYT")
        insertMaterias = self.insertsBuilder.materia(10, materiaN1, 1) + \
                         self.insertsBuilder.materia(11, materia_ConCorrelativa, 1, [10])

        insertUsuario = self.insertsBuilder.usuario(idUsuario, 123, "123")
        insertUsuarioxCarrera = self.insertsBuilder.usuarioxcarrera(idUsuario, 1)
        self.dbTesting.ejecutarComandosMult(insertUsuario+ insertCarreras+insertMaterias+ insertUsuarioxCarrera)

        response = self.middlewareTest.posiblesDelUsuario(idUsuario)
        self.assertIn(materiaN1, response)
        self.assertNotIn(materia_ConCorrelativa, response)


    def test_PosiblesMateriasParaUsuario_ConUnaMateriaAprobadas(self):
        """
        Test materias posibles para un usuario puede inscribirse en la materia con correlativa aprobada
        """
        idUsuario = 1
        materiaAprobada = 'Elementos de programación y lógica'
        materia_ConCorrelativa = 'Introduccion a la programacion'

        # Carga de datos
        insertCarreras = self.insertsBuilder.carrera(1, "Tecnicatura en Programacion Informatica", "CYT")
        insertMaterias = self.insertsBuilder.materia(10, materiaAprobada, 1) + \
                         self.insertsBuilder.materia(11, materia_ConCorrelativa, 1, [10])

        insertUsuario = self.insertsBuilder.usuario(idUsuario, 123, "123")
        insertUsuarioxCarrera = self.insertsBuilder.usuarioxcarrera(idUsuario, 1)
        insertUsuarioxMateria = self.insertsBuilder.usuarioxmateria(idUsuario, 10,7) # materia aprobada
        self.dbTesting.ejecutarComandosMult(insertUsuario+ insertCarreras+insertMaterias+ insertUsuarioxCarrera + insertUsuarioxMateria)

        response = self.middlewareTest.posiblesDelUsuario(idUsuario)
        self.assertIn(materia_ConCorrelativa, response)
        self.assertNotIn(materiaAprobada, response)

    def test_PosiblesMateriasParaUsuario_NoInscriptoACarrera(self):
        """
        Test materias posibles para un usuario puede inscribirse en la materia con correlativa aprobada
        """
        idUsuario = 1

        # Carga de datos
        insertUsuario = self.insertsBuilder.usuario(idUsuario, 123, "123")
        self.dbTesting.ejecutarComandosMult(insertUsuario)

        response = self.middlewareTest.posiblesDelUsuario(idUsuario)
        self.assertIn("No se encontraron materias", response)

if __name__ == '__main__':
    unittest.main()
