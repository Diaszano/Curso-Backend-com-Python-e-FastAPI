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
class RepositorioProduto():
    def __init__(self, db:Session) -> None:
        self.db = db;
    
    def criar(self, produto: schemas.Produto) -> models.Produto:
        db_produto = models.Produto(
            nome=produto.nome,
            detalhes=produto.detalhes,
            preco=produto.preco,
            disponivel=produto.disponivel 
        );

        self.db.add(db_produto);
        self.db.commit();
        self.db.refresh(db_produto);
        return db_produto;
    
    def listar(self) -> List[models.Produto]:
        produtos = self.db.query(models.Produto).all();
        return produtos;
    
    def obter(self,produto: schemas.Produto) -> None:
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