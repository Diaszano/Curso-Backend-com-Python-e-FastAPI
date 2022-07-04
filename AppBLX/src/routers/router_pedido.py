""""""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from fastapi import APIRouter, Depends, status, HTTPException
from src.routers.router_auth_utils import obter_usuario_logado
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
@router.get("/compras",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.PedidoSimples],
            tags=[NOME_TAG])
async def listar_meus_pedidos(  session:Session=Depends(get_db),
                                usuario:schemas.Usuario=Depends(
                                obter_usuario_logado)):
    
    lista_pedidos = RepositorioPedido(session).listarPedidos(
        usuario.id
    );
    return lista_pedidos;

@router.get("/vendas",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.PedidoRetorno],
            tags=[NOME_TAG])
async def listar_minhas_vendas( session:Session=Depends(get_db),
                                usuario:schemas.Usuario=Depends(
                                obter_usuario_logado)):
    
    lista_pedidos = RepositorioPedido(session).listarVendas(
        id=usuario.id
    );
    return lista_pedidos;

@router.get("/compras/{id}",
            status_code=status.HTTP_200_OK,
            response_model=schemas.PedidoRetorno,
            tags=[NOME_TAG])
async def pegar_pedido( id:int,session:Session=Depends(get_db),
                        usuario:schemas.Usuario=Depends(
                        obter_usuario_logado)):
    
    compra = RepositorioPedido(session).pegarCompra(
        idPedido=id,
        idUser=usuario.id
    );
    
    if(not compra):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pedido com id={id} inexistente!"
        );
    
    return compra;

@router.get("/vendas/{id}",
            status_code=status.HTTP_200_OK,
            response_model=schemas.PedidoRetorno,
            tags=[NOME_TAG])
async def pegar_venda(  id:int,session:Session=Depends(get_db),
                        usuario:schemas.Usuario=Depends(
                        obter_usuario_logado)):
    
    venda = RepositorioPedido(session).pegarVenda(
        idPedido=id,
        idUser=usuario.id
    );
    
    if(not venda):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pedido com id={id} inexistente!"
        );
    
    return venda;

@router.post(  "/inserir",
                status_code=status.HTTP_201_CREATED,
                response_model=schemas.PedidoSimples,
                tags=[NOME_TAG])
async def fazer_pedido( pedido:schemas.Pedido,
                        session:Session=Depends(get_db),
                        usuario:schemas.Usuario=Depends(
                        obter_usuario_logado)):
    
    pedido_criado = RepositorioPedido(session).criar(
        pedido=pedido,
        idUser=usuario.id
    );
    
    return pedido_criado;
#-----------------------
# Main()
#-----------------------
#-----------------------