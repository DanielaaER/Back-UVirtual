
from xmlrpc.client import SERVER_ERROR
from uvirtual.uv_library.bot.login import get_user_uv
import logging
from config.db import conn, engine
from models.estudiante import estudiantes
from schemas.estudiante import Estudiante, EstudianteAuth
from models.docente import docentes
from schemas.docente import Docente, DocenteAuth, DocenteUpdate
from fastapi import APIRouter, Response, Header
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from typing import List
from functions_jwt import write_token, validate_token
from werkzeug.security import generate_password_hash, check_password_hash
import json
from typing import Union

from data.login import login
loginRouter = APIRouter()



@loginRouter.post("/login")
def login_user(id_user, password):
    try:   
        print ("inicio")
        result = login(id_user, password)
        print(result)
        return result
    except Exception as exception_error:
        logging.error(
            f"Error al obtener información  ||| {exception_error}")
        return Response(status_code=500)
