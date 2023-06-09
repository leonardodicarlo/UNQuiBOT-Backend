from models.carrera import Carrera
from models.materia import Materia
from .bd.database import Database


class CarrerasDAO:
    def __init__(self):
        self.db = Database()

    def findCarreraById(self, id):
        sql = "select c.id, c.nombre, c.depto from carrera c where id = '" + str(id) + "'"
        carreraRes = self.db.execute_query(sql)
        if(not carreraRes):
            raise Exception("No se encontró carrera con id "+ str(id))

        sql = "select m.id, m.nombre from materia m join carrera_materias cm on m.id = cm.idMateria " \
              "where cm.idCarrera = " + str(id)
        materiasRes = self.db.execute_query(sql)

        carrera = Carrera(carreraRes[0])
        if materiasRes:
            carrera.materias = self.buildMaterias(list(materiasRes))

        return carrera


    def buildMaterias(self, dictMaterias):
        materias = []
        for dm in dictMaterias:
            materias.append(Materia(dm))
        return materias

    def materiasPorCarrera(self, idCarrera):
        sql = 'select idMateria from carrera_materias where idCarrera = {idCarrera}' \
            .format(idCarrera=idCarrera)
        return self.db.execute_query(sql)