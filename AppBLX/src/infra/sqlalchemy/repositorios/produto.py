"""Produtos"""
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
    
    def criar(self,id:int, produto: schemas.Produto) -> None:
        stmt = insert(models.Produto).values(
            nome       = produto.nome,
            detalhes   = produto.detalhes,
            preco      = produto.preco,
            disponivel = produto.disponivel,
            tamanhos   = produto.tamanhos,
            usuario_id = id
        );
        self.session.execute(stmt);
        self.session.commit();
    
    def listar(self,id:int) -> List[models.Produto]:
        stmt = select(models.Produto).where(
            models.Produto.usuario_id==id
        );
        produtos = self.session.execute(stmt).scalars().all();
        return produtos;
    
    def editar(self,idUser:int,idProduto:int,produto:schemas.Produto) -> None:
        stmt = update(models.Produto).where(
            (models.Produto.id==idProduto) &
            (models.Produto.usuario_id==idUser)
        ).values(
            nome       = produto.nome,
            detalhes   = produto.detalhes,
            preco      = produto.preco,
            disponivel = produto.disponivel,
            tamanhos   = produto.tamanhos
        );
        self.session.execute(stmt);
        self.session.commit();
    
    def buscarPorId(self,idProduto:int,idUser:int) -> models.Produto:
        stmt = select(models.Produto).where(
            (models.Produto.id==idProduto) &
            (models.Produto.usuario_id==idUser)
        );
        produto = self.session.execute(stmt).scalars().first();
        return produto;
    
    def remover(self,idProduto:int,idUser:int) -> None:
        stmt = delete(models.Produto).where(
            (models.Produto.id==idProduto) &
            (models.Produto.usuario_id==idUser)
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