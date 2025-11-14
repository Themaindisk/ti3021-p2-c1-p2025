import oracledb
import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")


def get_connection():
    return oracledb.connect(user=username, password=password, dsn=dsn)


def create_schema(query):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                print(f"Tabla creada \n {query}")
    except oracledb.DatabaseError as error:
        print(f"No se pudo crear la tabla: {error}")

tables = [
    (
        "CREATE TABLE  participante ("
        "id_numero_inscripcion INTEGER PRIMARY KEY,"
        "nombre VARCHAR(60),"
        "edad INTEGER(60)" 
        ");"
        
    )
    (
        "CREATE TABLE atleta ("
        "id_diciplinas VARCHAR(70),"
        "marca_personal FLOAT(100),"
        "categoria VARCHAR(70)"
        ");"
        
    )
    (
        "CREATE TABLE ENTRENADOR ("
        "equipo VARCHAR(70),"
        "plan_entrenamiento VARCHAR(70),"
        "especialidades VARCHAR(70)"
        ");"
        
    ) 
    (
        "CREATE TABLE JUEZ ("
        "reglamento VARCHAR(4000),"
        "certificado_valido VARCHAR(100),"
        "experiencia INTEGER(300)"
        ");"
        
        
        
        
        
        
        
    )    
        
        
        
        
        
        
    )
]

for query in tables:
    create_schema(query)