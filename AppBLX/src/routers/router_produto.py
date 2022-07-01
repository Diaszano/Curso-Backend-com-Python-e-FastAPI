""""""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
#-----------------------
# CONSTANTES
#-----------------------
router = APIRouter();
NOME_TAG = "Produtos";
#-----------------------
# CLASSES
#-----------------------
#-----------------------
# FUNÇÕES()
#-----------------------
@router.get(   "/produtos",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.Produto],
            tags=[NOME_TAG]
        )
def listar_produtos(session:Session=Depends(get_db)):
    lista_produtos = RepositorioProduto(session).listar();
    return lista_produtos;

@router.post(  "/produtos",
            status_code=status.HTTP_201_CREATED,
            response_model=schemas.Produto,
            tags=[NOME_TAG]
        )
def criar_produto(produto:schemas.Produto,session:Session=Depends(get_db)):
    produto_criado = RepositorioProduto(session).criar(produto);
    return produto_criado;

@router.put(  "/produtos/{id}",
            status_code=status.HTTP_200_OK,
            response_model=schemas.ProdutoSimples,
            tags=[NOME_TAG]
        )
def criar_produto(id:int,produto:schemas.Produto,session:Session=Depends(get_db)):
    RepositorioProduto(session).editar(id,produto);
    return produto;
#-----------------------
# Main()
#-----------------------
#-----------------------