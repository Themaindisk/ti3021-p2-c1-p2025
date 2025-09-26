class Partcipante:
    def __init__(self, nombre:str, edad:int, numero_inscripcion:str):
        self._nombre = nombre
        self._edad = edad
        self._numero_inscripcion = numero_inscripcion
        
class Atleta:
    def __init__(self, disciplinas:str, marca_personal:float, categoria:str):
        self._disciplinas = disciplinas
        self._marca_personal = marca_personal
        self._categoria = categoria
        
class Entrenador:
    def __init__(self, equipo:str, plan_entrenamiento:str, especialidades:str):
        self._equipo = equipo
        self._plan_entrenamiento = plan_entrenamiento
        self._especialidades = especialidades