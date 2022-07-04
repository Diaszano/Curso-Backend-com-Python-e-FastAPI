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

    def criarRetorno(   self,idUser:int,
                        produto: schemas.Produto) -> models.Produto:
        
        session_produto = models.Produto(
            nome       = produto.nome,
            detalhes   = produto.detalhes,
            preco      = produto.preco,
            disponivel = produto.disponivel,
            tamanhos   = produto.tamanhos,
            usuario_id = idUser
        );
        
        self.session.add(session_produto);
        self.session.commit();
        self.session.refresh(session_produto);
        return session_produto;

    def criar(self,idUser:int,produto: schemas.Produto) -> None:
        stmt = insert(models.Produto).values(
            nome       = produto.nome,
            detalhes   = produto.detalhes,
            preco      = produto.preco,
            disponivel = produto.disponivel,
            tamanhos   = produto.tamanhos,
            usuario_id = idUser
        );
        self.session.execute(stmt);
        self.session.commit();
    
    def listar(self,idUser:int) -> List[models.Produto]:
        stmt = select(models.Produto).where(
            models.Produto.usuario_id==idUser
        );
        produtos = self.session.execute(stmt).scalars().all();
        return produtos;
    
    def editar( self,idUser:int,idProduto:int,
                produto:schemas.Produto) -> None:
        
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