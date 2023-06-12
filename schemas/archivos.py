
from pydantic import BaseModel, EmailStr
from typing import Optional

class Archivos(BaseModel):
    id: Optional[int]
    matricula: Optional [str]
    credencial: Optional[str]
    video: Optional[str]