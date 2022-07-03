"""Produtos"""
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
class RepositorioProduto():
    def __init__(self, session:Session) -> None:
        self.session = session;

    def verificarId(self,id:int) -> bool:
        stmt = select(models.Produto).where(
            models.Produto.id==id
        );
        retorno  = self.session.execute(stmt).first();
        if(not retorno):
            return False;
        return True;
    
    def criar(self, produto: schemas.Produto) -> models.Produto:
        session_produto = models.Produto(
            nome       = produto.nome,
            detalhes   = produto.detalhes,
            preco      = produto.preco,
            disponivel = produto.disponivel,
            tamanhos   = produto.tamanhos,
            usuario_id = produto.usuario_id
        );

        self.session.add(session_produto);
        self.session.commit();
        self.session.refresh(session_produto);
        return session_produto;
    
    def listar(self) -> List[models.Produto]:
        stmt = select(models.Produto);
        produtos = self.session.execute(stmt).scalars().all();
        return produtos;
    
    def editar(self,id:int,produto:schemas.Produto) -> None:
        stmt = update(models.Produto).where(
            models.Produto.id==id
        ).values(
            nome       = produto.nome,
            detalhes   = produto.detalhes,
            preco      = produto.preco,
            disponivel = produto.disponivel,
            tamanhos   = produto.tamanhos
        );
        self.session.execute(stmt);
        self.session.commit();
    
    def buscarPorId(self,id:int) -> models.Produto:
        stmt = select(models.Produto).where(
            models.Produto.id==id
        );
        produto = self.session.execute(stmt).first();
        return produto;
    
    def remover(self,id:int) -> None:
        stmt = delete(models.Produto).where(
            models.Produto.id==id
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