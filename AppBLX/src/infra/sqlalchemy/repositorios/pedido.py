"""Modulo Models"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class RepositorioPedido():
    def __init__(self, db:Session) -> None:
        self.db = db;
    
    def criar(self, pedido: schemas.Pedido) -> models.Pedido:
        db_pedido = models.Pedido(
            quantidade=pedido.quantidade,
            entrega=pedido.entrega,
            endereco=pedido.endereco,
            observacoes=pedido.observacoes
        );

        self.db.add(db_pedido);
        self.db.commit();
        self.db.refresh(db_pedido);
        return db_pedido;
    
    def listar(self) -> List[models.Pedido]:
        pedidos = self.db.query(models.Pedido).all();
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