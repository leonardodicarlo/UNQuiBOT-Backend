class Carrera:
    id: int
    nombre: str
    depto: str
    materias: list

    def __init__(self, d=None):
        self.materias = []
        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)

    def infoMaterias(self):
        if not self.materias or len(self.materias) < 1:
            return "No existen materias cargadas."
        else:
            inf = ""
            for m in self.materias:
                inf = inf + "<br/> -" + m.nombre
            return inf
