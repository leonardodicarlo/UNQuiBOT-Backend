from models.carrera import Carrera
from persistence.carreraDAO import CarrerasDAO
from interface.interfazTemplate import InterfazTemplate

class InterfazMySQL(InterfazTemplate):

    def __init__(self):
        super().__init__()
        self.dao = CarrerasDAO()

    def getCarreraById(self, id:int) -> Carrera:
        """ Dado un ID de carrera, retorna una instancia de @Carrera """
        print("getCarreraById")
        return self.dao.findCarreraById(id)

    def getCantidadDeMateriasByCarreraId(self, id:int) -> int:
        """ Dado un ID de carrera, retorna la cantidad sus materias cargadas """
        print("getCantidadDeMateriasByCarreraId")
        return len(self.dao.findCarreraById(id).materias)
