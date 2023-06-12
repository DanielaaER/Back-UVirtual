from xmlrpc.client import SERVER_ERROR
import logging
from fastapi import APIRouter, Response, Header
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from werkzeug.security import generate_password_hash, check_password_hash
import json

passwordRouter = APIRouter()

@passwordRouter.get("/password")
def get_password():
    try:
        return get_clasees()
    except Exception as exception_error:
        logging.error(
            f"Error al obtener información de las clases ||| {exception_error}")
        return Response(status_code=500)
