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

    def infoMateria(self, id):
        dictMaterias = self.currentInterface.getInfoMateria(int(id))
        nombre_materia = dictMaterias[0]['nombreMateria']
        email_grupo = dictMaterias[0]['emailGrupo']
        horarios_aulas = []
        for item in dictMaterias:
            horarios_aulas.append(item['horarios'] + ' - ' + item['aulas'])
        horarios_aulas_str = '\n<br/>'.join(horarios_aulas)
        result = f'Materia: {nombre_materia}\n<br/>Lista de Mail: {email_grupo}\n\n<br/>Horarios y Aulas:\n{horarios_aulas_str}'
        return result

    def materiasAprobadasDelUsuario(self, usr):
        materiasAprobadas = self.currentInterface.getMateriasByUserId(usr)
        nombreMaterias = [x['nombre'] for x in materiasAprobadas]
        if len(materiasAprobadas) != 0:
            resp = "Tenés las siguientes materias aprobadas: <br/>" + " <br/>".join(nombreMaterias)
        else:
            resp = "Aún no tenés materias aprobadas"
        return resp

    def promedioDelUsuario(self, usr):
        promedio = self.currentInterface.promedioByUserId(usr)
        if promedio != 0:
            resp = "Tu promedio actual es: " + str(promedio)
        else:
            resp = "Aún no tenés notas cargadas"
        return resp