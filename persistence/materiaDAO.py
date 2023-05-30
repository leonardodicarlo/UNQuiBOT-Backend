from .bd.database import Database


class MateriaDAO:
    def __init__(self):
        self.db = Database()

    def getInfoMateriaById(self, idMateria):
        sql = 'select * from cursada where idMateria = {idMateria}' \
            .format(idMateria=idMateria)
        return self.db.execute_query(sql)

    def getCorrelativasById(self, idCarrera, idMateria):
        sql = 'select * from materias_correlativas where idMateria = {idMateria} and idCarrera = {idCarrera}' \
            .format(idMateria=idMateria, idCarrera=idCarrera)
        return self.db.execute_query(sql)
