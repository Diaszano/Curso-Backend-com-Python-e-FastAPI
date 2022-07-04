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
    
    def verificarId(self,id:int) -> bool:
        stmt = select(models.Pedido).where(
            models.Pedido.id==id
        );
        retorno  = self.session.execute(stmt).first();
        if(not retorno):
            return False;
        return True;

    def criar(self,idUser:int, pedido: schemas.Pedido) -> models.Pedido:
        session_pedido = models.Pedido(
            quantidade  = pedido.quantidade,
            entrega     = pedido.entrega,
            endereco    = pedido.endereco,
            observacoes = pedido.observacoes,
            usuario_id  = idUser,
            produto_id  = pedido.produto_id
        );

        self.session.add(session_pedido);
        self.session.commit();
        self.session.refresh(session_pedido);
        return session_pedido;
    
    def listarPedidos(self,id:int) -> List[models.Pedido]:
        stmt = select(models.Pedido).where(
            models.Pedido.usuario_id==id
        );
        pedidos = self.session.execute(stmt).scalars().all();
        return pedidos;
    
    def listarVendas(self,id:int) -> List[models.Pedido]:
        stmt = select(models.Pedido).join(
            models.Produto
        ).where(
            (models.Pedido.produto_id == models.Produto.id) &
            (models.Produto.usuario_id == id)
        );
        pedidos = self.session.execute(stmt).scalars().all();
        return pedidos;
    
    def pegarCompra(self,idPedido:int,idUser:int) -> models.Pedido:
        stmt = select(models.Pedido).where(
            (models.Pedido.usuario_id == idUser) &
            (models.Pedido.id == idPedido)
        );
        pedidos = self.session.execute(stmt).scalars().one_or_none();
        return pedidos;
    
    def pegarVenda(self,idPedido:int,idUser:int) -> models.Pedido:
        stmt = select(models.Pedido).join(
            models.Produto
        ).where(
            (models.Pedido.produto_id == models.Produto.id) &
            (models.Produto.usuario_id == idUser) &
            (models.Pedido.id == idPedido)
        );
        pedidos = self.session.execute(stmt).scalars().one_or_none();
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