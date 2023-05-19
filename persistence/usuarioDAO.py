from .bd.database import Database


class UsuarioDAO:
    def __init__(self):
        self.db = Database()

    def getAll(self):
        return self.db.execute_query("Select * from usuario")

    def getMateriasAprobadas(self, idUsuario):
        sql = 'select * from materia m where m.id in (' \
              'select idMateria from usuario_mcursadas where idUsuario = {idUsr} )' \
            .format(idUsr=idUsuario)
        return self.db.execute_query(sql)
