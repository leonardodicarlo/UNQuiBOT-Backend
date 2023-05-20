from .bd.database import Database


class MateriaDAO:
    def __init__(self):
        self._db = Database()

    def getInfoMateriaById(self, idMateria):
        sql = 'select * from cursada where idMateria = {idMateria}' \
            .format(idMateria=idMateria)
        return self._db.execute_query(sql)
