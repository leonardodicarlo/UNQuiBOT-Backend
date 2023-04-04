from bd.database import DataBase


class AlumnoDAO:
    def __init__(self):
        self._db = DataBase()

    def getAll(self):
        return self._db.execute_query("Select * from alumno")

    def getMateriasAprobadas(self, idAlumno):
        sql = 'select * from materia m where m.id in (' \
              'select idMateria from alumno_mcursadas where idAlumno = {idAl} )' \
            .format(idAl=idAlumno)
        return self._db.execute_query(sql)
