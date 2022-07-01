""""""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.pedido import RepositorioPedido
#-----------------------
# CONSTANTES
#-----------------------
router = APIRouter();
NOME_TAG = "Pedidos";
#-----------------------
# CLASSES
#-----------------------
#-----------------------
# FUNÇÕES()
#-----------------------
@router.get(   "/pedidos",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.Pedido],
            tags=[NOME_TAG]
        )
def listar_pedidos(session:Session=Depends(get_db)):
    lista_produtos = RepositorioPedido(session).listar();
    return lista_produtos;

@router.post(  "/pedidos",
            status_code=status.HTTP_201_CREATED,
            response_model=schemas.Pedido,
            tags=[NOME_TAG]
        )
def criar_pedidos(produto:schemas.Pedido,session:Session=Depends(get_db)):
    produto_criado = RepositorioPedido(session).criar(produto);
    return produto_criado;
#-----------------------
# Main()
#-----------------------
#-----------------------