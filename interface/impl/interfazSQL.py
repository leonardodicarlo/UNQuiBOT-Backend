from models.carrera import Carrera
from models.usuario import Usuario
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
        print("getCarreraById")
        return self.dao.findCarreraById(id)

    def getCantidadDeMateriasByCarreraId(self, id:int) -> int:
        """ Dado un ID de carrera, retorna la cantidad sus materias cargadas """
        print("getCantidadDeMateriasByCarreraId")
        return len(self.dao.findCarreraById(id).materias)

    def getInfoMateria(self, id:int) -> dict:
        """ Dado un ID de materia, retorna la información de la cursada actual para dicha materia"""
        print("getInfoMateria")
        return self.daoMateria.getInfoMateriaById(id)

    def getMateriasByUserId(self, id) -> Usuario:
        """ Dado un ID de usuario, retorna sus materias aprobadas """
        print("getMateriasByUserId")
        return self.daoUser.getMateriasAprobadas(id)

    def promedioByUserId(self, usr) -> float:
        """ Dado un ID de usuario, retorna el promedio de todas sus notas finales """
        print("promedioByUserId")
        return self.daoUser.getPromedio(usr)


