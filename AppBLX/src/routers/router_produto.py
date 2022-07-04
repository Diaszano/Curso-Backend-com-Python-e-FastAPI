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
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
#-----------------------
# CONSTANTES
#-----------------------
router   = APIRouter();
NOME_TAG = "Produtos";
#-----------------------
# CLASSES
#-----------------------
#-----------------------
# FUNÇÕES()
#-----------------------
@router.get("/listar",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ProdutoSimples],
            tags=[NOME_TAG])
async def listar_produtos(  session:Session=Depends(get_db),
                            usuario:schemas.Usuario=Depends(
                            obter_usuario_logado)
                        ):
    
    lista_produtos = RepositorioProduto(session).listar(usuario.id);
    return lista_produtos;

@router.post(   "/inserir",
                status_code=status.HTTP_201_CREATED,
                response_model=schemas.ProdutoSimples,
                tags=[NOME_TAG])
async def criar_produto(produto:schemas.ProdutoSimples,
                        session:Session=Depends(get_db),
                        usuario:schemas.Usuario=Depends(
                        obter_usuario_logado)):

    retorno = RepositorioProduto(session).criarRetorno(
        idUser=usuario.id,
        produto=produto
    );
    return retorno;

@router.put(  "/editar/{id}",
            status_code=status.HTTP_200_OK,
            response_model=schemas.ProdutoRetorno,
            tags=[NOME_TAG]
        )
async def editar_produto(   id:int,produto:schemas.Produto,
                            session:Session=Depends(get_db),
                            usuario:schemas.Usuario=Depends(
                            obter_usuario_logado)):
    
    verificar = RepositorioProduto(session).buscarPorId(
        idProduto=id,
        idUser=usuario.id
    );
    
    if(not verificar):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item com id={id} inexistente!"
        );
        
    RepositorioProduto(session).editar(
        idProduto=id,
        idUser=usuario.id,
        produto=produto
    );
    
    return produto;

@router.get("/pegar/{id}",
            status_code=status.HTTP_200_OK,
            response_model=schemas.ProdutoRetorno,
            tags=[NOME_TAG]
        )
async def exibir_produto(   id:int,session:Session=Depends(get_db),
                            usuario:schemas.Usuario=Depends(
                            obter_usuario_logado)):
    
    retorno = RepositorioProduto(session).buscarPorId(
        idProduto=id,
        idUser=usuario.id
    );
    
    if(not retorno):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item com id={id} inexistente!"
        );
    return retorno;

@router.delete(   "/remover/{id}",
            status_code=status.HTTP_200_OK,
            response_model=schemas.ProdutoRetorno,
            tags=[NOME_TAG]
        )
async def deletar_produto(   id:int,session:Session=Depends(get_db),
                            usuario:schemas.Usuario=Depends(
                            obter_usuario_logado)):
    
    retorno = RepositorioProduto(session).buscarPorId(
        idProduto=id,
        idUser=usuario.id
    );
    
    if(not retorno):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item com id={id} inexistente!"
        );
    
    RepositorioProduto(session).remover(
        idProduto=id,
        idUser=usuario.id
    );
    return retorno;
#-----------------------
# Main()
#-----------------------
#-----------------------