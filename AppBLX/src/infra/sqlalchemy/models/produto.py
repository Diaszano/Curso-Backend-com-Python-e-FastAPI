"""Produto - Models"""
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
class Produto(Base):
    """Produto - Models
    
    Neste modelo nós criamos a tabela dos produtos.
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
    
    # Modelo de Ligação N-1
    # 
    # Variável = Column(
    #     Integer, 
    #     ForeignKey(
    #         "Nome_da_tabela_que_queres_conectar.Seu_id", 
    #         name="Nome_da_chave"
    #     )
    # );
    # 
    # Variável = relationship(
    #     "Nome_da_classe",
    #     back_populates="Nome_da_variável_dentro_da_classe"
    # );

    # Ligação com o Usuário
    usuario_id = Column(
        Integer, 
        ForeignKey(
            "usuario.id", 
            name="fk_produto_usuario"
        )
    );

    usuario = relationship(
        "Usuario",
        back_populates="produtos"
    );

    # Modelo de Ligação 1-N
    # 
    # Variável = relationship(
    #     "Nome_da_classe",
    #     back_populates="Nome_da_variável_dentro_da_classe"
    # );

    # Ligação com o Pedido
    pedidos = relationship(
        "Pedido",
        back_populates='produto'
    );
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------