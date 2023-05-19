from .bd.database import Database


class UsuarioDAO:
    def __init__(self):
        self.db = Database()

    def getAll(self):
        return self.db.execute_query("Select * from usuario")

    def getMateriasAprobadas(self, idUsuario):
        sql = 'select * from materia m where m.id in (' \
              'select idMateria from usuario_mcursadas where idUsuario = {idUsr} and notaFinal > 3)' \
            .format(idUsr=idUsuario)
        return self.db.execute_query(sql)

    def getPromedio(self, idUsuario):
        sql = 'select notaFinal from usuario_mcursadas where idUsuario = {idUsr}' \
            .format(idUsr=idUsuario)
        notas = self.db.execute_query(sql)
        suma_notas = sum(nota['notaFinal'] for nota in notas)
        if len(notas) != 0:
            return suma_notas / len(notas)
        else:
            return 0
