CREATE TABLE
    PARTICIPANTES (
        nombre VARCHAR(60),
        edad INTEGER(60),
        numero_inscripcion INTEGER PRIMARY KEY,

    );


CREATE TABLE
    ATLETA (
       diciplinas VARCHAR(70),
       marca_personal FLOAT(100),
       categoria VARCHAR(70)
    );

CREATE TABLE
    ENTRENADOR (
        equipo VARCHAR(70),
        plan_entrenamiento VARCHAR(70),
        especialidades VARCHAR(70)
    )