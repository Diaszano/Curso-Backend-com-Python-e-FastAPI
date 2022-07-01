"""AppBLX"""
#-----------------------
# BIBLIOTECAS
#-----------------------
import sys
from src.schemas import schemas
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from src.infra.sqlalchemy.config.database import get_db, criar_db
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
@app.get("/usuarios")
def listar_usuarios(db:Session=Depends(get_db)):
    lista_produtos = RepositorioUsuario(db).listar();
    return lista_produtos;

@app.post("/usuarios",status_code=201)
def criar_usuarios(produto:schemas.Usuario,db:Session=Depends(get_db)):
    produto_criado = RepositorioUsuario(db).criar(produto);
    return produto_criado;

# Produto
@app.get("/produtos")
def listar_produtos(db:Session=Depends(get_db)):
    lista_produtos = RepositorioProduto(db).listar();
    return lista_produtos;

@app.post("/produtos",status_code=201)
def criar_produto(produto:schemas.Produto,db:Session=Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto);
    return produto_criado;

# Pedido
@app.get("/pedidos")
def listar_pedidos(db:Session=Depends(get_db)):
    lista_produtos = RepositorioPedido(db).listar();
    return lista_produtos;

@app.post("/pedidos",status_code=201)
def criar_pedidos(produto:schemas.Pedido,db:Session=Depends(get_db)):
    produto_criado = RepositorioPedido(db).criar(produto);
    return produto_criado;
#-----------------------
# Main()
#-----------------------
#-----------------------