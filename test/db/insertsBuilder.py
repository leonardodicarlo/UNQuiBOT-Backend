
pref = "INSERT INTO"


class InsertScriptBuilder:

    def carrera(self, id: int, nombre: str, depto: str):
        return f"{pref} carrera(id, nombre, depto) VALUES ({id}, '{nombre}', '{depto}');"

    def materia(self, id: int, nombre: str, idCarrera: int):
        return f"{pref} materia(id, idCarrera, nombre) VALUES ({id}, {idCarrera},'{nombre}');" \
               f"{pref} carrera_materias (idCarrera,idMateria) VALUES ({idCarrera},{id});"

    def usuario(self, id: int, dni: int, legajo: str):
        return f"{pref} usuario(id, dni, legajo) VALUES ({id}, {dni}, '{legajo}');"

    def usuarioxmateria(self, id: int, idMateria: int, nota: int):
        return f"{pref} usuario_mcursadas (idUsuario,idMateria,notaFinal) VALUES({id}, {idMateria}, {nota});"

    def cursada(self, id: int, idMateria: int, comision: int, nombreMateria: str, emailGrupo: str, horarios: str, periodo: str, activa, aulas: str):
        return f"{pref} cursada (id,idMateria,comision,nombreMateria,emailGrupo,horarios,periodo,activa,aulas) " \
               f"VALUES ({id},{idMateria},{comision},'{nombreMateria}','{emailGrupo}','{horarios}','{periodo}',{activa},'{aulas}');"
