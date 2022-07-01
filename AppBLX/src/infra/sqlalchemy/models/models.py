"""Modulo Models"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, Float
from sqlalchemy import ForeignKey, Integer,String
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
    senha    = Column(String);

    # Ligação com o Produto
    produtos = relationship("Produto",back_populates='usuario');
    # Ligação com o Pedido
    # pedidos = relationship("Produto",back_populates='usuario');

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
    tamanhos   = Column(String);
    
    # Ligação com o Usuário
    usuario_id = Column(
        Integer, 
        ForeignKey(
            "usuario.id", 
            name="fk_usuario"
        )
    );
    usuario    = relationship("Usuario",back_populates="produtos");

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