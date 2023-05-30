from models.carrera import Carrera
from models.materia import Materia

class InterfazTemplate:

    def getCarreraById(self, id:int) -> Carrera:
        """ Dado un ID de carrera, retorna una instancia de la clase @Carrera """
        pass

    def getCantidadDeMateriasByCarreraId(self, id:int) -> int:
        """ Dado un ID de carrera, retorna la cantidad sus materias cargadas """
        pass

    def getInfoMateria(self, id:int) -> dict:
        """ Dado un ID de materia, retorna la información de la cursada actual para dicha materia"""
        pass

    def getMateriasByUserId(self, usr) -> [Materia]:
        """ Dado un ID de usuario, retorna sus materias aprobadas """
        pass

    def promedioByUserId(self, usr) -> float:
        """ Dado un ID de usuario, retorna el promedio de todas sus notas finales """
        pass

    def posiblesByUserId(self, usr) -> [Materia]:
        """ Dado un ID de usuario, retorna las posibles materias a las que puede anotarse """
        pass