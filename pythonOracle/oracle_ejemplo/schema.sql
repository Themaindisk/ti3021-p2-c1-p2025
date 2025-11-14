CREATE TABLE PARTICIPANTES (
        nombre VARCHAR(60),
        edad INTEGER(60),
        numero_inscripcion INTEGER PRIMARY KEY

    );


CREATE TABLE ATLETA (
       diciplinas INTEGER (70),
       marca_personal FLOAT(100),
       categoria VARCHAR(70)
    );

CREATE TABLE ENTRENADOR (
        equipo INTEGER(70),
        plan_entrenamiento VARCHAR(70),
        especialidades VARCHAR(70)
    );

CREATE TABLE JUEZ (
    id_juez INTEGER PRIMARY KEY,
    reglamento VARCHAR(4000),
    certificado_valido VARCHAR(100),
    experiencia INTEGER(300)
)