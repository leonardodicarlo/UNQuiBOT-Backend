from .bd.database import Database


class MateriaDAO:
    def __init__(self):
        self.db = Database()

    def getInfoMateriaById(self, idMateria):
        sql = 'select * from cursada where idMateria = {idMateria}' \
            .format(idMateria=idMateria)
        return self.db.execute_query(sql)
