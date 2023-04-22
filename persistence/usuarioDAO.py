from bd.database import Database


class UsuarioDAO:
    def __init__(self):
        self._db = Database()

    def getAll(self):
        return self._db.execute_query("Select * from usuario")

    def getMateriasAprobadas(self, idUsuario):
        sql = 'select * from materia m where m.id in (' \
              'select idMateria from usuario_mcursadas where idUsuario = {idUsr} )' \
            .format(idUsr=idUsuario)
        return self._db.execute_query(sql)
