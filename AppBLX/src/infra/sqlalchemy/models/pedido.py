"""Pedido - Models"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from sqlalchemy import Boolean, Column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Integer,String
from src.infra.sqlalchemy.config.database import Base
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
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
            name="fk_pedido_usuario"
        )
    );

    usuario = relationship(
        "Usuario",
        back_populates="pedidos"
    );

    # Ligação com o Produto
    produto_id = Column(
        Integer, 
        ForeignKey(
            "produto.id", 
            name="fk_pedido_produto"
        )
    );

    produto = relationship(
        "Produto",
        back_populates="pedidos"
    );
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------