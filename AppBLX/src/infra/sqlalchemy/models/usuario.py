"""Usuário - Models"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from sqlalchemy import Column
from sqlalchemy import Integer,String
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class Usuario(Base):
    """Usuário - Models
    
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

    # Modelo de Ligação 1-N
    # 
    # Variável = relationship(
    #     "Nome_da_classe",
    #     back_populates="Nome_da_variável_dentro_da_classe"
    # );

    # Ligação com o Produto
    produtos = relationship(
        "Produto",
        back_populates='usuario'
    );
    # Ligação com o Pedido
    pedidos = relationship(
        "Pedido",
        back_populates='usuario'
    );
    
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------