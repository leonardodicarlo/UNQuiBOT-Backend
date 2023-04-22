class Usuario:
    def __init__(self, id, legajo, dni):
        self._id = id
        self._legajo = legajo
        self._dni = dni
        self._carreras = {}
        self._mat_aprobadas = {}
