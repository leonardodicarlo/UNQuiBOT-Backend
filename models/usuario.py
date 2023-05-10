class Usuario:
    id: int
    legajo: str
    dni: int
    carreras: list
    mat_aprobadas: list
    def __init__(self, id, legajo, dni):
        self.id = id
        self.legajo = legajo
        self.dni = dni
        self.carreras = []
        self.mat_aprobadas = []