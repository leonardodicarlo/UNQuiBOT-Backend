from interface.interfazTemplate import InterfazTemplate
from interface.impl.interfazSQL import InterfazMySQL


class Interfaz:

    currentInterface: InterfazTemplate = InterfazMySQL()

    def infoMateriasPorCarrera(self, id):
        carrera = self.currentInterface.getCarreraById(int(id))
        infoCarrera = "Las materias de la carrera " + carrera.nombre + " son: " \
                    + carrera.infoMaterias()
        return infoCarrera

    def cantidadMateriasPorCarrera(self, id):
        carrera = self.currentInterface.getCarreraById(int(id))
        cantidadMaterias = "La carrera " + carrera.nombre + " tiene " \
                        + str(len(carrera.materias)) + " materias"
        return cantidadMaterias