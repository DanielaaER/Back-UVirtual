
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


from data.estudiante import ingresar_estudiantee

from data.docente import  login_docentee


def login(id_user, password):
    with engine.connect() as conn:
        
        if id_user[0].lower() in ['z', 's']:
            tipo = "Student"
            print(tipo)
            log = EstudianteAuth
            log.matricula=id_user
            log.contraseña=password
            log.correo=None
            result = ingresar_estudiantee(log)
        else:
            tipo = "Docente"
            print(tipo)
            log = DocenteAuth
            log.id=id_user
            log.contraseña=password
            log.correo=None
            print("hello")
            print("buscara")
            result = login_docentee(log)
            print("encontro")
            print(result)
        if result is None:
            print("..............................")
            return Response(status_code=HTTP_204_NO_CONTENT)
        print(result)
        return {
            "user" : tipo,
            "data" : result
        }