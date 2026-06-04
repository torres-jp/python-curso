# APIREST: Interfaz de Programación de Aplicaciones para compartir recursos a través de la web. Permite a los desarrolladores interactuar con servicios y datos de manera estructurada.

import uuid

from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Inicialización de la aplicación FastAPI
app = FastAPI()


# Definición del modelo de datos para un curso utilizando Pydantic
class Curso(BaseModel):
    id: Optional[str] = None  # El ID se generará automáticamente al crear un curso
    nombre: str
    description: Optional[str] = None
    nivel: str
    duracion: int


# Base de datos simulada para almacenar los cursos
cursos_db = []


# CRUD: READ (Obtener todos los cursos)
@app.get("/cursos/", response_model=list[Curso])
def obtener_cursos():
    return cursos_db


# CRUD: CREATE (Agregar un nuevo curso)
@app.post("/cursos/", response_model=Curso)
def crear_curso(curso: Curso):
    curso.id = str(uuid.uuid4())  # Generar un ID único para el curso
    cursos_db.append(curso)
    return curso


# CURD: GET (individual) Leeremos el curso que coincida con el ID que buscamos.
@app.get("/cursos/{curso_id}", response_model=Curso)
def obtener_curso(curso_id: str):
    curso = next(
        (curso for curso in cursos_db if curso.id == curso_id), None
    )  # Con next toma la primera coincidencia y None si no lo encuentra. Es mas eficiente que for.
    if curso is None:
        raise HTTPException(status_code=404, details="Curso no encontrado")
    return curso


# CRUD: UPDATE  PUT (Actualizar) Actualizaremos el recurso según el id proporcionado.
@app.put("/cursos/{curso_id}", response_model=Curso)
def actualizar_curso(curso_id: str, curso_actualizado: Curso):
    curso = next(
        (curso for curso in cursos_db if curso.id == curso_id), None
    )  # Con next toma la primera coincidencia y None si no lo encuentra. Es mas eficiente que for.
    if curso is None:
        raise HTTPException(status_code=404, details="Curso no encontrado")
    curso_actualizado.id = curso_id
    index = cursos_db.index(curso)  # Buscamos el indice del curso a actualizar.
    cursos_db[index] = curso_actualizado  # Actualizamos el curso
    return curso_actualizado


# CRUD: DELETE (Eliminar) Eliminaremos el recurso según el id proporcionado.
@app.delete("/cursos/{curso_id}", response_model=Curso)
def eliminar_curso(curso_id: str):
    curso = next(
        (curso for curso in cursos_db if curso.id == curso_id), None
    )  # Con next toma la primera coincidencia y None si no lo encuentra. Es mas eficiente que for.
    if curso is None:
        raise HTTPException(status_code=404, details="Curso no encontrado")
    cursos_db.remove(curso)  # Eliminamos el curso
    return curso
