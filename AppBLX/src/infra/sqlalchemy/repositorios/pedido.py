"""Pedidos"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy import models
from sqlalchemy import select, update, delete
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class RepositorioPedido():
    def __init__(self, session:Session) -> None:
        self.session = session;
    
    def verificar_id(self,id:int) -> bool:
        stmt = select(models.Pedido).where(
            models.Pedido.id==id
        );
        retorno  = self.session.execute(stmt).first();
        if(not retorno):
            return False;
        return True;

    def criar(self, pedido: schemas.Pedido) -> models.Pedido:
        session_pedido = models.Pedido(
            quantidade  = pedido.quantidade,
            entrega     = pedido.entrega,
            endereco    = pedido.endereco,
            observacoes = pedido.observacoes,
            usuario_id  = pedido.usuario_id,
            produto_id  = pedido.produto_id
        );

        self.session.add(session_pedido);
        self.session.commit();
        self.session.refresh(session_pedido);
        return session_pedido;
    
    def listar(self) -> List[models.Pedido]:
        stmt = select(models.Pedido);
        pedidos = self.session.execute(stmt).scalars().all();
        return pedidos;
    
    def editar(self,id:int,pedido:schemas.Pedido) -> None:
        stmt = update(models.Pedido).where(
            models.Pedido.id==id
        ).values(
            quantidade  = pedido.quantidade,
            entrega     = pedido.entrega,
            endereco    = pedido.endereco,
            observacoes = pedido.observacoes
        );
        self.session.execute(stmt);
        self.session.commit();
    
    def remover(self,id:int) -> None:
        stmt = delete(models.Pedido).where(
            models.Pedido.id==id
        )
        self.session.execute(stmt);
        self.session.commit();
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------