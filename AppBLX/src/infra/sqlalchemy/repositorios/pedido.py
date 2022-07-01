"""Pedidos"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from src import schemas
from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.infra.sqlalchemy import models
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class RepositorioPedido():
    def __init__(self, session:Session) -> None:
        self.session = session;
    
    def criar(self, pedido: schemas.Pedido) -> models.Pedido:
        session_pedido = models.Pedido(
            quantidade  = pedido.quantidade,
            entrega     = pedido.entrega,
            endereco    = pedido.endereco,
            observacoes = pedido.observacoes
        );

        self.session.add(session_pedido);
        self.session.commit();
        self.session.refresh(session_pedido);
        return session_pedido;
    
    def listar(self) -> List[models.Pedido]:
        stmt = select(models.Pedido);
        pedidos = self.session.execute(stmt).scalars().all();
        return pedidos;
    
    def obter(self) -> None:
        pass;
    
    def remover(self) -> None:
        pass;
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------