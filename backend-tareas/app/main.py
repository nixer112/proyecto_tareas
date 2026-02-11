from fastapi import FastAPI
from .database import engine, Base
from fastapi.middleware.cors import CORSMiddleware # <--- IMPORTANTE
from .routers import tareas

# 1. CREAR TABLAS
# Esto le dice a SQLAlchemy: "Mira mis modelos (models.py) y si alguna tabla
# no existe en la base de datos, créala ahora mismo".
# Como ya creamos 'tareas' a mano con SQL, esto no hará nada malo,
# pero es vital si añades nuevas tablas en el futuro.
Base.metadata.create_all(bind=engine)

# 2. INICIALIZAR LA APP
app = FastAPI(
    title="Gestor de Tareas API",
    description="API REST para gestionar tareas con Angular y MySQL",
    version="1.0.0"
)

origins = [
    "http://localhost:4200", # El puerto por defecto de Angular
    "http://localhost:3000", # Por si usas otro framework algún día
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # Qué dominios permitimos
    allow_credentials=True,     # Cookies y tokens de autenticación
    allow_methods=["*"],        # Métodos permitidos (GET, POST, PUT, DELETE...)
    allow_headers=["*"],        # Cabeceras permitidas
)

# 3. CONECTAR RUTAS
# Aquí es donde "enchufamos" el archivo de rutas que acabas de crear.
app.include_router(tareas.router)

# Ruta raíz para comprobar que funciona
@app.get("/")
def read_root():
    return {"mensaje": "¡Bienvenido a la API de Tareas! Visita /docs para ver la documentación."}
