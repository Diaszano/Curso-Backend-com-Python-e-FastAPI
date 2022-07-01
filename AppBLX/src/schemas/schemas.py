"""Modulo schemas"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from pydantic import BaseModel
from typing import List, Optional
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class Usuario(BaseModel):
    """Usuario - Schema
    
    Neste modelo nós criamos todos os dados 
    necessários para a criação de um usuários 
    no nosso programa.
    """
    id      : Optional[int] = None;
    nome    : str;
    telefone: str;
    senha   : str;

    class Config:
        orm_mode = True;

class Produto(BaseModel):
    """Produto - Schema
    
    Neste modelo nós criamos todos os dados 
    necessários para a criação de um produto
    no nosso programa.
    """
    id        : Optional[int] = None;
    nome      : str;
    detalhes  : str;
    preco     : float;
    disponivel: bool = False;
    tamanhos  : Optional[str] = "Não informado";
    usuario_id: int;
    
    class Config:
        orm_mode = True;

class Pedido(BaseModel):
    """Pedido - Schema
    
    Neste modelo nós criamos todos os dados 
    necessários para a criação de um pedido
    no nosso programa.
    """
    id         : Optional[int] = None;
    quantidade : int;
    entrega    : bool = False;
    endereco   : str;
    observacoes: Optional[str] = "Sem observações";

    class Config:
        orm_mode = True;
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------