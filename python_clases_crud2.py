from datetime import date

class Persona:
    def __init__(
            self, 
            rut: str, 
            nombre: str, 
            apellidos: str, 
            fecha_nacimiento: date,
            cod_area = int 
            telefono: int
    ):
        self.rut = rut
        self.nombres = nombres
        self.apellidos: str = apellidos
        self.fecha_nacimiento: date = fecha_nacimiento
        self.cod_area:  int = cod_area
        self.telefono: int = telefono
        pass

def create_persona():
    rut = input("ingresa el rut de la persona: ")
    nombres = input("ingresa los nombres de la persona: ")
    apellidos = input("ingresa los apellidos de la persona: ")
    dia_nacimiento = (int("ingresa el dia de nacimiento de la persona: "))
    mes_nacimiento = (int("ingresa el mes de nacimento de la perosna: "))
    anio_nacimiento = (int("ingresa el anio de nacimiento de la persona: "))
    fecha_nacimiento:date = input("ingresa la fecha de nacimiento de la persona: ")
    cod_area: int = input("ingresa el codigo de area del telefono de la persona: ")
    telefono: int = input("ingresa el numero de telefono de la persona: ")
    persona = persona(
        rut = rut,
        nombres = nombres,
        apellidos = apellidos,
        fecha_nacimiento = fecha_nacimiento,
        cod_area = cod_area,
        telefono = telefono,
        persona = persona
    )
    if persona_existe(persona):
        return print(f"la persona con el rut {persona.rut} ya existe. intente con otro rut.")

    
    
    
    personas.append(persona)

def
    


personas: list = [Persona] = []