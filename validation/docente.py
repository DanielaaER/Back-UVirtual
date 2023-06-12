
from schemas.user import userAuth;

import re

def validar_loginDocente(docente_Data):
    if docente_Data.id is not None:
        if not validar_id(docente_Data.id):
            return False
    # if user_Data.correo is not None:
    #     if not validar_email(user_Data.correo):
    #         return False
    return True


def validar_Docente(docente_Data):
    
    if docente_Data.correo is not None:
        if not validar_email(docente_Data.correo):
            return False
    if docente_Data.telefono is not None:
        if not validar_telefono(docente_Data.telefono):
            return False
    if docente_Data.campus is not None:
        if not validar_campus(docente_Data.campus):
            return False
    return True


def validar_campus(campus: str) -> bool:
    patron = r'^\D+$'
    return bool(re.match(patron, campus))


def validar_id(id: str) -> bool:
    patron = r'^\d+$'
    return bool(re.match(patron, id))



def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(patron, email))

def validar_telefono(telefono: str) -> bool:
    patron = r'^\d{10}$'
    return bool(re.match(patron, telefono))
