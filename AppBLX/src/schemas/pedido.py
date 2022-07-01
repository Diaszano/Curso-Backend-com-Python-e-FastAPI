"""Pedido - Schema"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import Optional
from pydantic import BaseModel
from src.schemas.usuario import Usuario
from src.schemas.produto import Produto
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class Pedido(BaseModel):
    """Pedido - Schema
    
    Neste schema nós criamos todos os dados 
    necessários para a criação de um pedido
    no nosso programa.
    """
    id         : Optional[int] = None;
    quantidade : int;
    entrega    : bool = False;
    endereco   : str;
    observacoes: Optional[str] = "Sem observações";
    usuario_id : Optional[int] = None;
    usuario    : Optional[Usuario] = None;
    produto_id : Optional[int] = None;
    produto    : Optional[Produto] = None;

    class Config:
        orm_mode = True;
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------