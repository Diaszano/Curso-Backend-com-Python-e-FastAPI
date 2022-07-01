"""Produtos"""
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
class RepositorioProduto():
    def __init__(self, session:Session) -> None:
        self.session = session;
    
    def criar(self, produto: usuario.Produto) -> usuario.Produto:
        session_produto = usuario.Produto(
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
    
    def listar(self) -> List[usuario.Produto]:
        stmt = select(usuario.Produto);
        produtos = self.session.execute(stmt).scalars().all();
        return produtos;
    
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