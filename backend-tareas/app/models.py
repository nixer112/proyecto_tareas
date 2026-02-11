#Vamos a pensar que esto es el diccionario traductor
# Aqui definimos las tablas de la base de datos, cada clase es una tabla 
# y cada atributo es una columna

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.sql import func
from .database import Base

class Tarea(Base):
    __tablename__ = "tareas" #nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True, index=True) #id es la clave primaria y se indexa para mejorar la velocidad de las consultas
    titulo = Column(String(255), nullable=False)     
    descripcion = Column(Text, nullable=True)
    completada = Column(Boolean, default=False) #por defecto no esta completada
    created_at = Column(DateTime, server_default=func.now()) #fecha de creacion, se asigna automaticamente al crear la tarea

