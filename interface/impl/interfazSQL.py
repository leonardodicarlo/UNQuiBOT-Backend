from models.carrera import Carrera
from models.usuario import Usuario
from models.materia import Materia
from persistence.carreraDAO import CarrerasDAO
from persistence.usuarioDAO import UsuarioDAO
from persistence.materiaDAO import MateriaDAO
from interface.interfazTemplate import InterfazTemplate

class InterfazMySQL(InterfazTemplate):

    def __init__(self):
        super().__init__()
        self.dao = CarrerasDAO()
        self.daoUser = UsuarioDAO()
        self.daoMateria = MateriaDAO()

    def getCarreraById(self, id:int) -> Carrera:
        """ Dado un ID de carrera, retorna una instancia de @Carrera """
        return self.dao.findCarreraById(id)

    def getCantidadDeMateriasByCarreraId(self, id:int) -> int:
        """ Dado un ID de carrera, retorna la cantidad sus materias cargadas """
        return len(self.dao.findCarreraById(id).materias)

    def getInfoMateria(self, id:int) -> dict:
        """ Dado un ID de materia, retorna la información de la cursada actual para dicha materia"""
        return self.daoMateria.getInfoMateriaById(id)

    def getMateriasByUserId(self, usr) -> [Materia]:
        """ Dado un ID de usuario, retorna sus materias aprobadas """
        return self.daoUser.getMateriasAprobadas(usr)

    def promedioByUserId(self, usr) -> float:
        """ Dado un ID de usuario, retorna el promedio de todas sus notas finales """
        return self.daoUser.getPromedio(usr)

    def posiblesByUserId(self, usr) -> [Materia]:
        """ Dado un ID de usuario, retorna las posibles materias a las que puede anotarse """
        aprobadas = self.daoUser.getMateriasAprobadas(usr)
        idAprobadas = list(map(lambda x: x['id'], aprobadas))
        carrera = self.daoUser.getCarrera(usr)
        materiasCarrera = self.dao.materiasPorCarrera(carrera[0]['idCarrera'])
        cursables = []

        for materia in materiasCarrera:
            if materia['idMateria'] not in idAprobadas:
                correlativas = self.daoMateria.getCorrelativasById(carrera[0]['idCarrera'],materia['idMateria'])
                idCorrelativas = list(map(lambda x: x['idCorrelativa'], correlativas))
                esCursable = all(elemento in idAprobadas for elemento in idCorrelativas)
                if esCursable:
                    cursables.append(materia)
        print(cursables)
        return cursables



        return self.daoUser.getMateriasAprobadas(usr)
