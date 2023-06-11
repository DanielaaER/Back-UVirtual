
from pydantic import BaseModel, EmailStr
from typing import Optional

class userAuth(BaseModel):
    id: Optional [int]
    matricula: Optional [str]
    correo: Optional[str]
    contraseña: str