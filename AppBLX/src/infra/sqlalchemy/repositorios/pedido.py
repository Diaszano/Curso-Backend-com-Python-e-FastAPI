"""Pedidos"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from sqlalchemy import select
from src.schemas import usuario
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import usuario
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class RepositorioPedido():
    def __init__(self, session:Session) -> None:
        self.session = session;
    
    def criar(self, pedido: usuario.Pedido) -> usuario.Pedido:
        session_pedido = usuario.Pedido(
            quantidade  = pedido.quantidade,
            entrega     = pedido.entrega,
            endereco    = pedido.endereco,
            observacoes = pedido.observacoes
        );

        self.session.add(session_pedido);
        self.session.commit();
        self.session.refresh(session_pedido);
        return session_pedido;
    
    def listar(self) -> List[usuario.Pedido]:
        stmt = select(usuario.Pedido);
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