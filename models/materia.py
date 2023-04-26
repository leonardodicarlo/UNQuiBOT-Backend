class Materia:
    id: int
    nombre: str
    idCarrera: int
    correlativas: list

    def __init__(self, d=None):
        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)
        self.correlativas = []
