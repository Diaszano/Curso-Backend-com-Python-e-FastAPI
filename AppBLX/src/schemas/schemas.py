"""Modulo schemas"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List, Optional
from pydantic import BaseModel
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
    id           : Optional[str] = None;
    nome         : str;
    telefone     : str;
    # meus_produtos: List[Produto];
    # minhas_vendas: List[Pedido];
    # meus_pedidos : List[Pedido];

    class Config:
        orm_mode = True;

class Produto(BaseModel):
    """Produto - Schema
    
    Neste modelo nós criamos todos os dados 
    necessários para a criação de um produto
    no nosso programa.
    """
    id        : Optional[str] = None;
    # usuario   : Usuario;
    nome      : str;
    detalhes  : str;
    preco     : float;
    disponivel: bool = False;

    class Config:
        orm_mode = True;

class Pedido(BaseModel):
    """Pedido - Schema
    
    Neste modelo nós criamos todos os dados 
    necessários para a criação de um pedido
    no nosso programa.
    """
    id         : Optional[str] = None;
    # usuario    : Usuario;
    # produto    : Produto;
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