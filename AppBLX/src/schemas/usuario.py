"""Usuário - Schema"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from pydantic import BaseModel
from typing import List, Optional
from src.schemas.pedido import Pedido
from src.schemas.produto import Produto
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class Usuario(BaseModel):
    """Usuário - Schema
    
    Neste schema nós criamos todos os dados 
    necessários para a criação de um usuários 
    no nosso programa.
    """
    id      : Optional[int] = None;
    nome    : str;
    telefone: str;
    senha   : str;
    produtos: Optional[List[Produto]] = None;
    pedidos : Optional[List[Pedido]]  = None;

    class Config:
        orm_mode = True;
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------