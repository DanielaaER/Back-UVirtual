
from xmlrpc.client import SERVER_ERROR
from uvirtual.uv_library.bot.horario import get_class_uv
import logging
from config.db import conn, engine
from models.estudiante import estudiantes
from schemas.estudiante import Estudiante, EstudianteAuth
from models.clase import clases
from schemas.clase import Clase
from fastapi import APIRouter, Response, Header
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from typing import List
from functions_jwt import write_token, validate_token
from werkzeug.security import generate_password_hash, check_password_hash
import json
from sqlalchemy.sql import text
from models.horarioDocente import horarioDocentes
from schemas.horarioDocente import HorarioDocente


from data.horarioDocente import get_horarioDocentees, get_HorarioDocente_id
horarioDocenteRouter = APIRouter()


@horarioDocenteRouter.get("/horarioDocente", response_model=List[HorarioDocente])
def get_horarioDocente():
    try:
        return get_horarioDocentees()
    except Exception as exception_error:
        logging.error(
            f"Error al obtener información de las clases ||| {exception_error}")
        return Response(status_code=500)


@horarioDocenteRouter.get("/horarioDocente/horarioDocente/{id_docente}", response_model=List[Clase])
def get_HorarioDocente_by_Docente(id_docente: int):
    try:

        return get_HorarioDocente_id(id_docente)
    except Exception as exception_error:
        logging.error(
            f"Error al obtener información de las clases ||| {exception_error}")
        return Response(status_code=500)
