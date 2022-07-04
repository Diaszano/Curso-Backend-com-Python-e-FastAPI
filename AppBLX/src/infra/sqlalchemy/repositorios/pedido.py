"""Pedidos"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy import models
from sqlalchemy import select, update, delete, insert
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class RepositorioPedido():
    def __init__(self, session:Session) -> None:
        self.session = session;

    def criarRetorno(   self,idUser:int,
                        pedido:schemas.Pedido)->models.Pedido:
        
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
    
    def criar(self,idUser:int, pedido: schemas.Pedido) -> None:
        stmt = insert(models.Pedido).values(
            quantidade  = pedido.quantidade,
            entrega     = pedido.entrega,
            endereco    = pedido.endereco,
            observacoes = pedido.observacoes,
            usuario_id  = idUser,
            produto_id  = pedido.produto_id
        );
        self.session.execute(stmt);
        self.session.commit();
    
    def listarPedidos(self,idUser:int) -> List[models.Pedido]:
        stmt = select(models.Pedido).where(
            models.Pedido.usuario_id==idUser
        );
        pedidos = self.session.execute(stmt).scalars().all();
        return pedidos;
    
    def listarVendas(self,idUser:int) -> List[models.Pedido]:
        stmt = select(models.Pedido).join(
            models.Produto
        ).where(
            (models.Pedido.produto_id == models.Produto.id) &
            (models.Produto.usuario_id == idUser)
        );
        pedidos = self.session.execute(stmt).scalars().all();
        return pedidos;
    
    def pegarCompra(self,idPedido:int,idUser:int) -> models.Pedido:
        stmt = select(models.Pedido).where(
            (models.Pedido.usuario_id == idUser) &
            (models.Pedido.id == idPedido)
        );
        pedidos = self.session.execute(stmt).scalars().first();
        return pedidos;
    
    def pegarVenda(self,idPedido:int,idUser:int) -> models.Pedido:
        stmt = select(models.Pedido).join(
            models.Produto
        ).where(
            (models.Pedido.produto_id == models.Produto.id) &
            (models.Produto.usuario_id == idUser) &
            (models.Pedido.id == idPedido)
        );
        pedidos = self.session.execute(stmt).scalars().first();
        return pedidos;
    
    def editar(self,idPedido:int,pedido:schemas.Pedido) -> None:
        stmt = update(models.Pedido).where(
            models.Pedido.id==idPedido
        ).values(
            quantidade  = pedido.quantidade,
            entrega     = pedido.entrega,
            endereco    = pedido.endereco,
            observacoes = pedido.observacoes
        );
        self.session.execute(stmt);
        self.session.commit();
    
    def remover(self,idPedido:int) -> None:
        stmt = delete(models.Pedido).where(
            models.Pedido.id==idPedido
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