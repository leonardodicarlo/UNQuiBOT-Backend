class Materia:

    def __init__(self, id,codigo, nombre):
        self._id = id
        self._codigo = codigo
        self._nombre = nombre
        self._correlativas = {}