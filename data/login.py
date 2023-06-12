
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

from validation.user import validar_user


def login(user_Data):
    with engine.connect() as conn:
        print(validar_user(user_Data))
        if validar_user(user_Data):
            result = None  # Inicializar result como None
            print(user_Data)
            if user_Data.matricula[0].lower() in ['z', 's'] :
                tipo = "Student"
                print(tipo)
                print(user_Data)
                result = ingresar_estudiantee(user_Data)
            else:
                tipo = "Docente"
                print(tipo)
                print("hello")
                print("buscara")
                
                user_Data.id=user_Data.matricula
                user_Data.matricula = None
                result = login_docentee(user_Data)
                print("encontro")
                print(result)
                
            if result is None:
                print("..............................")
                return Response(status_code=HTTP_204_NO_CONTENT)
            
            return {
                "user": tipo,
                "data": result
            }
        else:
            return Response(status_code=400)
