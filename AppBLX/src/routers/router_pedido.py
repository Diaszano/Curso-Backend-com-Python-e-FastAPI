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
async def listar_pedidos(session:Session=Depends(get_db)):
    lista_pedidos = RepositorioPedido(session).listar();
    return lista_pedidos;

@router.post(  "/pedidos",
            status_code=status.HTTP_201_CREATED,
            response_model=schemas.Pedido,
            tags=[NOME_TAG]
        )
async def criar_pedidos(pedido:schemas.Pedido,session:Session=Depends(get_db)):
    pedido_criado = RepositorioPedido(session).criar(pedido);
    return pedido_criado;
#-----------------------
# Main()
#-----------------------
#-----------------------