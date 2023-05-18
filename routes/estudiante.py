
from xmlrpc.client import SERVER_ERROR
from uvirtual.uv_library.bot.login import get_user_uv
import logging
from config.db import conn, engine
from models.estudiante import estudiantes
from schemas.estudiante import Estudiante, EstudianteAuth
from fastapi import APIRouter, Response, Header
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from typing import List
from functions_jwt import write_token, validate_token
from werkzeug.security import generate_password_hash, check_password_hash
import json


from data.estudiante import get_estudiantee, get_estudiantees, create_estudiantee, ingresar_estudiantee
estudianteRouter = APIRouter()


@estudianteRouter.get("/estudiantes", response_model=List[Estudiante])
def get_estudiantes():
    try:

        return get_estudiantees()
    except Exception as exception_error:
        logging.error(
            f"Error al obtener información de los estudiantes ||| {exception_error}")
        return Response(status_code=SERVER_ERROR)


@estudianteRouter.get("/estudiante/estudiante/{id_estudiante}", response_model=Estudiante)
def get_estudiante_by_id_estudiante(id_estudiante: int):
    try:

        return get_estudiantee(id_estudiante)

    except Exception as exception_error:
        logging.error(
            f"Error al obtener información del estudiante con el ID : {id_estudiante} ||| {exception_error}")
        return Response(status_code=SERVER_ERROR)


@estudianteRouter.post("/estudiantes")
def create_estudiante(data_estudiante: Estudiante):
    try:

       return create_estudiantee(data_estudiante)
    except Exception as exception_error:
        return Response(status_code=SERVER_ERROR)


@estudianteRouter.post("/estudiante", status_code=HTTP_201_CREATED)
def estudiantes_ingresar_al_sistema(estudiantes_auth: EstudianteAuth):
    try:
        return ingresar_estudiantee(estudiantes_auth)
    except Exception as exception_error:
        logging.error(f"Error al crear información del estudiante ")
        return {
            "status": 404,
            "message": "User not found",
        }


@estudianteRouter.post("/estudiante/verify/token")
def estudiantes_verificar_token(token_estudiante: str = Header(default=None)):
    # token = user_token.split(' ')[1]
    token = token_estudiante.split(" ")[0]
    return validate_token(token_estudiante, output=True)
