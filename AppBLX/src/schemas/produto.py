"""Produto - Schema"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import Optional
from pydantic import BaseModel
from src.schemas.usuario import Usuario;
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class Produto(BaseModel):
    """Produto - Schema
    
    Neste schema nós criamos todos os dados 
    necessários para a criação de um produto
    no nosso programa.
    """
    id        : Optional[int] = None;
    nome      : str;
    detalhes  : str;
    preco     : float;
    disponivel: bool = False;
    tamanhos  : Optional[str] = "Não informado";
    usuario_id: Optional[int] = None;
    usuario   : Optional[Usuario] = None;
    
    class Config:
        orm_mode = True;
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------