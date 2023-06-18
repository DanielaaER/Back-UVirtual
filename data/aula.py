

from xmlrpc.client import SERVER_ERROR
import logging
from config.db import conn, engine
from fastapi import APIRouter, Response, Header
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED

from models.aula import aulas
from schemas.aula import Aula


from functions_jwt import write_token, validate_token

def get_aulas():
    with engine.connect() as conn:
        result = conn.execute(aulas.select()).fetchall()
        aula_list = []
        for row in result:
            aula_dict = {
                "id": row[0],
                "nombre": row[1],
                "id_edificio": row[2],
                "password": row[3],
                "id_aula": row[4]
            }
            aula = Aula(**aula_dict)
            aula_list.append(aula_dict)
        
        if (result):
            logging.info(f"Se obtuvo información de todos los edifcios")
            
            return aula_list
        else:
            return Response(status_code=HTTP_204_NO_CONTENT)

            
def get_aulas_id(id):
    with engine.connect() as conn:
        result = conn.execute(aulas.select().where(aulas.c.id==id)).first()
        
        aula_dict = {
            "id": result[0],
            "nombre": result[1],
            "id_edificio": result[2],
            "password": result[3],
            "id_aula": result[4]
        }
            
        if (result):
            logging.info(f"Se obtuvo información de la aula")
            
            return aula_dict
        else:
            return Response(status_code=HTTP_204_NO_CONTENT)


def login_aula(aula_auth):
    with engine.connect() as conn:
        if (aula_auth.correo != None):
            result = conn.execute(docentes.select().where(aulas.c.correo == aula_auth.correo)).first()
        if (aula_auth.matricula != None):
            result = conn.execute(aulas.select().where(aulas.c.id_aula == aula_auth.matricula)).first()
            
        if result != None:
        
            if result[3] == aula_auth.contraseña:
                    
                return {
                    "status": 200,
                    "message": "Access success",
                    "token": write_token(aula_auth.dict()),
                    "user": get_aulas_id(result[0])
                }
            else:
                return Response(status_code=HTTP_401_UNAUTHORIZED)

        else:
            return Response(status_code=HTTP_204_NO_CONTENT)
    