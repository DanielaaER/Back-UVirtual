
from schemas.user import userAuth;

import re

def validar_loginEstudiante(student_Data):
    if student_Data.matricula is not None:
        if not validar_matricula(student_Data.matricula):
            return False
    # if user_Data.correo is not None:
    #     if not validar_email(user_Data.correo):
    #         return False
    return True


def validar_Estudiante(student_Data):
    if student_Data.matricula is not None:
        if not validar_matricula(student_Data.matricula):
            return False
    if student_Data.correo is not None:
        if not validar_email(student_Data.correo):
            return False
    if student_Data.telefono is not None:
        if not validar_telefono(student_Data.telefono):
            return False
    return True


def validar_matricula(matricula):
    patron = r'^([Zz][Ss]\d{8}|\d+)$'
    return bool(re.match(patron, matricula))



def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(patron, email))

def validar_telefono(telefono: str) -> bool:
    patron = r'^\d{10}$'
    return bool(re.match(patron, telefono))
