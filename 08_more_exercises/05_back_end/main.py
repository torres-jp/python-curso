# APIREST: Interfaz de Programación de Aplicaciones para compartir recursos a través de la web. Permite a los desarrolladores interactuar con servicios y datos de manera estructurada.

from typing import Optional
import uuid

from fastapi import FastAPI
from pydantic import BaseModel

# Inicialización de la aplicación FastAPI
app = FastAPI()


# Definición del modelo de datos para un curso utilizando Pydantic
class Curso(BaseModel):
    id: str
    nombre: str
    description: Optional[str] = None
    nivel: str
    duracion: int


# Base de datos simulada para almacenar los cursos
cursos_db = []


# CRUD: READ (Obtener todos los cursos)
@app.get("/cursos/", response_model=List[Curso])
def obtener_cursos():
    return cursos_db


# CRUD: CREATE (Agregar un nuevo curso)
@app.post("/cursos/", response_model=Curso)
def crear_curso(curso: Curso):
    curso.id = str(uuid.uuid4())  # Generar un ID único para el curso
    cursos_db.append(curso)
