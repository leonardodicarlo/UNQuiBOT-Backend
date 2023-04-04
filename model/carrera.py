class Carrera:
    def __init__(self, id, codigo, nombre, depto):
        self._id = id
        self._codigo = codigo
        self._nombre = nombre
        self._materias = {}
        self._depto = depto