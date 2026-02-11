from sqlalchemy.orm import Session
from . import models, schemas


# 1. LEER (READ)
def get_tareas(db: Session, skip: int = 0, limit: int = 100):
    # Esta función debe devolver una lista de tareas.
    # En SQL sería: SELECT * FROM tareas LIMIT 100 OFFSET 0;

    # PISTA: Usa db.query(models.Tarea)...
    return db.query(models.Tarea).offset(skip).limit(limit).all()


# 2. CREAR (CREATE)
def create_tarea(db: Session, tarea: schemas.TareaCreate):
    # Aquí recibimos el esquema 'TareaCreate' (titulo, descripcion...)
    # Pero la DB necesita un modelo 'models.Tarea'.

    # PASO 1: Crear la instancia del modelo ORM
    # db_tarea = models.Tarea(titulo=..., descripcion=...)
    # Truco Pro: usa **tarea.model_dump() para desempaquetar el diccionario
    db_tarea = models.Tarea(**tarea.model_dump())

    # PASO 2: Añadir a la sesión (preparar el SQL INSERT)
    # TODO: db.add(...)
    db.add(db_tarea)
    # PASO 3: Confirmar cambios (Ejecutar el SQL)
    # TODO: db.commit()
    db.commit()

    # PASO 4: Refrescar la instancia (Para obtener el ID generado y la fecha)
    # TODO: db.refresh(...)
    db.refresh(db_tarea)

    return db_tarea
