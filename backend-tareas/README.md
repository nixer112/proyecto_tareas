# 📝 Proyecto: Gestión de Tareas (Task Manager)

¡Bienvenido! Este es un proyecto personal desarrollado por **hobby** y con un enfoque 100% educativo. El objetivo principal es profundizar en el desarrollo de APIs modernas y aplicaciones web modulares, integrando nuevas herramientas a mi stack tecnológico.

---

## 🛠️ Stack Tecnológico

Para este proyecto he seleccionado tecnologías que destacan por su rendimiento y estructura:

* **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python)
    * **Pydantic:** Para validación de datos y tipado robusto.
    * **SQLAlchemy:** Como ORM para interactuar con la base de datos de forma eficiente.
* **Base de Datos:** [MySQL](https://www.mysql.com/) para el almacenamiento de datos relacionales.
* **Frontend:** [Angular](https://angular.io/) aprovechando su potente sistema de modularidad y componentes.

---

## 🚀 Configuración del Backend

Este proyecto utiliza **uv** para una gestión de paquetes ultra rápida.

1. **Instalar dependencias:**
   ```bash
   cd backend-tareas
   uv sync

# 🗺️ Roadmap: Gestor de Tareas Full Stack

Este documento rastrea el progreso del desarrollo de la aplicación "Gestor de Tareas", desde la concepción hasta el despliegue, siguiendo buenas prácticas de arquitectura de software.

---

## 🏗️ Fase 1: Infraestructura y Persistencia (Base de Datos)
*Objetivo: Establecer una base de datos robusta y accesible.*

- [x] **Instalación de MySQL Server** (Ubuntu Server / Local).
- [x] **Configuración de Red:** Habilitar conexiones remotas (`bind-address`, usuario remoto `%`).
- [x] **Diseño del Esquema (SQL):** Crear base de datos y tabla `tareas` con restricciones (`NOT NULL`, `DEFAULT`).
- [x] **Verificación:** Conexión exitosa desde el entorno de desarrollo (Workbench/DBeaver).

---

## 🐍 Fase 2: Backend (Python & FastAPI)
*Objetivo: Crear una API RESTful tipada, validada y escalable.*

### 2.1 Configuración
- [x] **Gestión de Entorno:** Inicializar proyecto con `uv` (o `venv`).
- [x] **Dependencias:** Instalar FastAPI, Uvicorn, SQLAlchemy, PyMySQL, Pydantic.
- [x] **Conexión DB:** Configurar `database.py` con SQLAlchemy Engine y SessionLocal.

### 2.2 Modelado de Datos
- [x] **ORM Models (`models.py`):** Mapear tabla SQL a clases Python (SQLAlchemy).
- [x] **Schemas (`schemas.py`):** Definir contratos de datos y validación (Pydantic).

### 2.3 Lógica de Negocio (CRUD)
- [x] **Repositorio (`crud.py`):** Funciones para Leer, Crear, Actualizar y Borrar tareas (aislando la DB de la API).
- [x] **Rutas (`routers/tareas.py`):** Definir endpoints HTTP (`GET`, `POST`, `PUT`, `DELETE`).
- [x] **Inyección de Dependencias:** Usar `get_db` en las rutas.

### 2.4 Configuración Avanzada
- [x] **CORS:** Configurar middleware para permitir peticiones desde Angular (localhost:4200).
- [x] **Refactorización:** Asegurar que `main.py` esté limpio e incluya los routers.

---

## 🅰️ Fase 3: Frontend (Angular 21)
*Objetivo: Interfaz moderna, reactiva y basada en componentes.*

### 3.1 Configuración
- [ ] **Setup:** Crear proyecto Angular con soporte para `Standalone Components`.
- [ ] **Estilos:** Configurar framework CSS (Tailwind o CSS modular limpio).
- [ ] **Modelos:** Crear interfaces TypeScript (`Task`) que coincidan con los Schemas de Python.

### 3.2 Arquitectura y Estado
- [ ] **Servicio HTTP:** Crear `TaskService` para comunicarse con FastAPI.
- [ ] **Gestión de Estado:** Implementar **Signals** para manejar la lista de tareas de forma reactiva.

### 3.3 Componentes (UI)
- [ ] **Task List:** Componente para mostrar las tareas.
- [ ] **Task Item:** Componente individual para cada tarea (con acciones de completar/borrar).
- [ ] **Task Form:** Formulario para crear nuevas tareas con validación.

---

## 🚀 Fase 4: Integración y Pulido Final
*Objetivo: Unificar el sistema y asegurar la calidad.*

- [ ] **Conexión Real:** Verificar que Angular recibe datos reales de MySQL vía FastAPI.
- [ ] **Feedback de Usuario:** Añadir indicadores de carga (loading spinners) y manejo de errores.
- [ ] **Limpieza:** Eliminar logs, comentarios temporales y código muerto.
- [ ] **Documentación:** Finalizar README con instrucciones de despliegue.

---

## 📂 Estructura del Proyecto

```text
/
├── backend/            # FastAPI + MySQL
│   ├── app/
│   │   ├── routers/
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── ...
│   └── pyproject.toml
│
├── frontend/           # Angular 17+
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/
│   │   │   ├── services/
│   │   │   └── models/
│   └── angular.json
│
└── README.md
