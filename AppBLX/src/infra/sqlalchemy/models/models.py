"""Modulo Models"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from sqlalchemy import Boolean, Column, Float, Integer,String
from src.infra.sqlalchemy.config.database import Base
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class Usuario(Base):
    """Usuario - Models
    
    Neste modelo nós criamos a tabela dos usuários.
    """
    __tablename__ = "usuario";

    id = Column(
        Integer,
        primary_key=True,
        index=True
    );
    nome     = Column(String);
    telefone = Column(String, unique=True);

class Produto(Base):
    """Usuario - Models
    
    Neste modelo nós criamos a tabela dos usuários.
    """
    __tablename__ = "produto";

    id = Column(
        Integer,
        primary_key=True,
        index=True
    );
    nome       = Column(String);
    detalhes   = Column(String);
    preco      = Column(Float);
    disponivel = Column(Boolean);

class Pedido(Base):
    """Pedido - Models
    
    Neste modelo nós criamos a tabela dos pedidos.
    """
    __tablename__ = "pedido";

    id = Column(
        Integer,
        primary_key=True,
        index=True
    );
    # usuario     = Column();
    # produto     = Column();
    quantidade  = Column(Integer);
    entrega     = Column(Boolean);
    endereco    = Column(String);
    observacoes = Column(String);


#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------