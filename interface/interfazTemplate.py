from models.carrera import Carrera
from models.usuario import Usuario

class InterfazTemplate:

    def getCarreraById(self, id:int) -> Carrera:
        """ Dado un ID de carrera, retorna una instancia de la clase @Carrera """
        pass

    def getCantidadDeMateriasByCarreraId(self, id:int) -> int:
        """ Dado un ID de carrera, retorna la cantidad sus materias cargadas """
        pass

    def getMateriasByUserId(self, usr) -> Usuario:
        """ Dado un ID de usuario, retorna sus materias aprobadas """
        pass