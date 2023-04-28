
class Cursada:

    id: int
    idMateria: int
    emailGrupo: str
    horarios: str
    docentes: str
    periodo: str
    activa: int
    aulas: str

    def __init__(self, d=None):
        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)