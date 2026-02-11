-- 1. Crear la Base de Datos (Schema)
-- Usamos utf8mb4 para soporte completo de caracteres (emojis, acentos)

CREATE DATABASE IF NOT EXISTS gestor_tareas_db 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

USE gestor_tareas_db;

-- 2. Crear la Tabla de Tareas
CREATE TABLE IF NOT EXISTS tareas (
    -- ID: Entero, autoincremental (1, 2, 3...) y Llave Primaria
    id INT AUTO_INCREMENT PRIMARY KEY,

    -- Titulo: Texto hasta 255 chars, OBLIGATORIO (NOT NULL)
    titulo VARCHAR(255) NOT NULL,

    -- Descripcion: Texto largo, OPCIONAL (puede ser NULL)
    descripcion TEXT,

    -- Completada: MySQL no tiene BOOLEAN nativo, usa TINYINT(1).
    -- 0 = Falso (Pendiente), 1 = Verdadero (Completada).
    -- DEFAULT 0 asegura que al crearla, nazca como "pendiente".
    completada TINYINT(1) DEFAULT 0,

    -- Created_at: Marca de tiempo automática.
    -- Se llena sola cuando insertas el registro.
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);