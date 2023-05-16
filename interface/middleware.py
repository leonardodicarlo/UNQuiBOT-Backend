from interface.interfazTemplate import InterfazTemplate
from interface.impl.interfazSQL import InterfazMySQL


class Middleware:

    def __init__(self, interface=InterfazMySQL()):
        self.currentInterface: InterfazTemplate = interface

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


    def materiasAprobadasDelUsuario(self, usr):
        materiasAprobadas = self.currentInterface.getMateriasByUserId(usr)
        nombreMaterias = [x['nombre'] for x in materiasAprobadas]
        resp = "Tenés las siguientes materias aprobadas: <br/>" + " <br/>".join(nombreMaterias)
        return resp