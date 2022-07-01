"""AppBLX"""
#-----------------------
# BIBLIOTECAS
#-----------------------
import sys
from typing import List
from src.schemas import schemas
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, status
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.pedido import RepositorioPedido
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
#-----------------------
# CONSTANTES/GLOBAIS
#-----------------------
sys.dont_write_bytecode = True;
app = FastAPI();
#-----------------------
# CLASSES
#-----------------------
#-----------------------
# FUNÇÕES()
#-----------------------
# Usuário
@app.get(  "/usuarios",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.Usuario]
        )
def listar_usuarios(session:Session=Depends(get_db)):
    lista_produtos = RepositorioUsuario(session).listar();
    return lista_produtos;

@app.post(  "/usuarios",
            status_code=status.HTTP_201_CREATED,
            response_model=schemas.Usuario
        )
def criar_usuarios(produto:schemas.Usuario,session:Session=Depends(get_db)):
    produto_criado = RepositorioUsuario(session).criar(produto);
    return produto_criado;

# Produto
@app.get(   "/produtos",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.Produto]
        )
def listar_produtos(session:Session=Depends(get_db)):
    lista_produtos = RepositorioProduto(session).listar();
    return lista_produtos;

@app.post(  "/produtos",
            status_code=status.HTTP_201_CREATED,
            response_model=schemas.Produto
        )
def criar_produto(produto:schemas.Produto,session:Session=Depends(get_db)):
    produto_criado = RepositorioProduto(session).criar(produto);
    return produto_criado;

# Pedido
@app.get(   "/pedidos",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.Pedido]
        )
def listar_pedidos(session:Session=Depends(get_db)):
    lista_produtos = RepositorioPedido(session).listar();
    return lista_produtos;

@app.post(  "/pedidos",
            status_code=status.HTTP_201_CREATED,
            response_model=schemas.Pedido
        )
def criar_pedidos(produto:schemas.Pedido,session:Session=Depends(get_db)):
    produto_criado = RepositorioPedido(session).criar(produto);
    return produto_criado;
#-----------------------
# Main()
#-----------------------
#-----------------------