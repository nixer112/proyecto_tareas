from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, models, schemas
from ..database import get_db

# 1. Configuración del Router
# prefix="/tareas": Todas las rutas empezarán por /tareas
# tags=["tareas"]: Para agruparlas bonito en la documentación automática
router = APIRouter(
    prefix="/tareas",
    tags=["tareas"]
)

# 2. RUTA LEER (GET /tareas/)
# response_model=List[schemas.Tarea]: Importante para que FastAPI filtre los datos
# y devuelva JSON limpio usando tu esquema Pydantic.
@router.get("/", response_model=List[schemas.Tarea])
def read_tareas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # TU TURNO: Llama a la función del CRUD que hicimos antes
    tareas = crud.get_tareas(db, skip=skip, limit=limit)
    return tareas

# 3. RUTA CREAR (POST /tareas/)
@router.post("/", response_model=schemas.Tarea)
def create_tarea(tarea: schemas.TareaCreate, db: Session = Depends(get_db)):
    # TU TURNO: Llama a la función create_tarea del CRUD
    tarea_creada = crud.create_tarea(db, tarea)
    return tarea_creada
