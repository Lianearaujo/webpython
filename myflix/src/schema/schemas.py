from pydantic import BaseModel
from typing import Optional

class Serie(BaseModel):
    id : Optional[str] = None
    nome: str
    genero: str
    ano: int
    qtd_temporadas: int
    class Config:
        orm_mode = True