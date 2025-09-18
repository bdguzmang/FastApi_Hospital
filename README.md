# 🏥 API de Hospitales - Práctica 02 (FastAPI + PostgreSQL)

Este proyecto implementa un **microservicio REST** usando **FastAPI** y **PostgreSQL** para la gestión de hospitales y usuarios.  
Forma parte de la **Práctica 02** del curso de Inteligencia Artificial / Desarrollo Backend.

---

## 🚀 Características

- CRUD completo para **hospitales** y **usuarios**.
- Validaciones de datos con **Pydantic**.
- Persistencia en **PostgreSQL** usando **SQLAlchemy ORM**.
- Documentación interactiva con **Swagger UI** (`/docs`).
- Configuración mediante archivo `.env`.

---

## 📂 Estructura del Proyecto

```
app/
 ├── api/
 │    └── routes/
 │        ├── health.py
 │        ├── hospitals.py
 │        └── usuarios.py 
 ├── core/ 
 │     └── config.py 
 ├── db/ 
 │     ├── base.py 
 │     └── session.py 
 ├── models/ 
 │     ├── hospital.py 
 │     └── usuario.py 
 └── schemas/ 
      ├── hospital.py
      └── usuario.py    
docker-compose.yml
requirements.txt
.env.example
schema.sql

```

---

## 🛠️ Requisitos

- Python 3.10 o superior  
- PostgreSQL 14+  
- Git  

---

## ⚙️ Instalación y Configuración

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/bdguzmang/FastApi_Hospital.git
cd FastApi_Hospital
```

### 2️⃣ Crear entorno virtual e instalar dependencias
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3️⃣ Configurar variables de entorno
Copia el archivo de ejemplo y ajusta tu contraseña de PostgreSQL:
```bash
cp .env.example .env
```

Contenido de `.env.example`:
```dotenv
DATABASE_URL=postgresql+psycopg2://appuser:TuContraseña@localhost:5432/appdb
```

### 4️⃣ Crear base de datos y tablas
En PostgreSQL:
```sql
CREATE DATABASE appdb OWNER appuser;
```

Luego ejecuta el script `schema.sql`:
```bash
psql -U appuser -d appdb -h localhost -f schema.sql
```

Contenido de `schema.sql` (ya incluido en el repositorio):
```sql
CREATE TABLE IF NOT EXISTS hospital (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    ciudad VARCHAR(120) NOT NULL,
    direccion VARCHAR(200) NOT NULL,
    creado_en TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS usuario (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    email VARCHAR(160) NOT NULL UNIQUE,
    rol VARCHAR(20) NOT NULL CHECK (rol IN ('admin','medico','asistente')),
    hospital_id INTEGER NOT NULL REFERENCES hospital(id) ON DELETE RESTRICT,
    creado_en TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

---

## ▶️ Ejecución del Servidor

```bash
uvicorn main:app --reload
```

La API estará disponible en:
- **Swagger UI:** http://localhost:8000/docs  
- **ReDoc:** http://localhost:8000/redoc  

---

## 📌 Ejemplos de Uso

### Crear un hospital
```bash
curl -X POST "http://localhost:8000/hospitals" \
-H "Content-Type: application/json" \
-d '{"nombre":"Hospital Central","ciudad":"Bogotá","direccion":"Calle 123 #45-67"}'
```

### Crear un usuario
```bash
curl -X POST "http://localhost:8000/usuarios" \
-H "Content-Type: application/json" \
-d '{"nombre":"Juan Pérez","email":"juan@example.com","rol":"medico","hospital_id":1}'
```

---

## 🧪 Pruebas

Si agregas tests con `pytest`, ejecútalos así:
```bash
pytest
```

---

## 👥 Equipo

|     Nombre    |      Rol      |
|---------------|---------------|
| Brayan GUzman | Desarrollador |


---

## 📄 Licencia

Proyecto con fines educativos. Uso libre para prácticas de aprendizaje.
