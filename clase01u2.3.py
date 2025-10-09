class Partcipante:
    def __init__(self, nombre:str, edad:int, numero_inscripcion:str):
        self._nombre = nombre
        self._edad = edad
        self._numero_inscripcion = numero_inscripcion
        
    @staticmethod
    def participar():
        pass
    
    @property
    def numero_inscripcion(self):
        return self.numero_inscripcion
    
    @staticmethod
    def nombre():
        pass        
        
          
class Atleta:
    def __init__(self, disciplinas:str, marca_personal:float, categoria:str):
        self._disciplinas = disciplinas
        self._marca_personal = marca_personal
        self._categoria = categoria

    @staticmethod
    def participar():
        pass
    
    @property
    def marca_personal(self):
        return self.marca_personal
    
    @staticmethod
    def disiplinas():
        pass

    
        
class Entrenador:
    def __init__(self, equipo:str, plan_entrenamiento:str, especialidades:str):
        self._equipo = equipo
        self._plan_entrenamiento = plan_entrenamiento
        self._especialidades = especialidades
        
    @staticmethod
    def participar():
        pass
    
    @property
    def plan_entrenamineto(self):
        return self.plan_entrenamineto
    
    @staticmethod
    def equipo():
        pass        
        
class Juez:
    def __init__(self, reglamento:str, certificado:bool, experiencia:int):
        self._reglamento = reglamento
        self._certificado = certificado
        self._experiencia = experiencia
        
    @staticmethod
    def participar():
        pass
    
    @property
    def certificado(self):
        return self.certificado
    
    @staticmethod
    def experiencia():
        pass        
        
   
        
        
        
        
           