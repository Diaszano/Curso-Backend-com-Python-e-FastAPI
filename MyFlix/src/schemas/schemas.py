"""Schemas"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from pydantic import BaseModel
from typing import List, Optional
#-----------------------
# CONSTANTES/GLOBAIS
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class Serie(BaseModel):
    id            : Optional[int] = None;
    titulo        : str;
    ano           : int;
    sinopse       : str;
    qtd_temporadas: int;

    class Config:
        orm_mode = True;

class Filme(BaseModel):
    id     : Optional[int] = None;
    titulo : str;
    ano    : int;
    sinopse: str;

    class Config:
        orm_mode = True;

#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------