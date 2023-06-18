
from schemas.user import userAuth;

import re

def validar_user(user_Data):
    # if user_Data.id is not None:
    #     if not validar_id(user_Data.id):
    #         return False
    if user_Data.matricula is not None:
        if not validar_matricula(user_Data.matricula):
            return False
    # if user_Data.correo is not None:
    #     if not validar_email(user_Data.correo):
    #         return False
    return True


def validar_matricula(matricula):
    patron = r'^(\d+|ZS\d{8}|aula\d{1,2}|\d)$'
    return bool(re.match(patron, matricula))



def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(patron, email))