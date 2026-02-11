from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TareaBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    completada: bool = False

class TareaCreate(TareaBase):
    pass

class Tarea(TareaBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True #Nos permite crear un objeto Tarea a partir de un objeto TareaModel (de SQLAlchemy) usando el método from_orm()
