from app.database import engine
from sqlalchemy import text

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT VERSION()"))
        print(f"✅ ¡Conexión exitosa! Versión de MySQL: {result.scalar()}")
except Exception as e:
    print(f"❌ Error al conectar: {e}")
