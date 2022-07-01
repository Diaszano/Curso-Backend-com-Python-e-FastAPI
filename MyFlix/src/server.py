"""MyFlix"""
#-----------------------
# BIBLIOTECAS
#-----------------------
import sys
from pydantic import BaseModel
from src.schemas import schemas
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from src.infra.sqlalchemy.config.database import get_db,criar_db
from src.infra.sqlalchemy.repositorios.serie import RepositorioSerie
from src.infra.sqlalchemy.repositorios.filme import RepositorioFilme
#-----------------------
# CONSTANTES/GLOBAIS
#-----------------------
sys.dont_write_bytecode = True;
criar_db();
app = FastAPI();
#-----------------------
# CLASSES
#-----------------------
class Titulo(BaseModel):
    titulo:str;
#-----------------------
# FUNÇÕES()
#-----------------------
# Série
@app.post("/series",status_code=201)
def criar_serie(serie:schemas.Serie,db:Session=Depends(get_db)) -> schemas.Serie:
    retorno = RepositorioSerie(db).criar(serie);
    return retorno;

@app.get("/series")
def pegar_series(db:Session=Depends(get_db)) -> dict:
    retorno = RepositorioSerie(db).listar();
    return retorno;

@app.get("/series/{id}")
def pegar_serie(id:int,db:Session=Depends(get_db)) -> dict:
    retorno = RepositorioSerie(db).obter(id);
    return retorno;

@app.get("/series/titulo")
def pegar_serie(titulo:Titulo,db:Session=Depends(get_db)) -> dict:
    titulo = titulo.titulo;
    retorno = RepositorioSerie(db).obter_titulo(titulo);
    return retorno;

@app.delete("/series/{id}")
def pegar_serie(id:int,db:Session=Depends(get_db)) -> dict:
    RepositorioSerie(db).remover(id);
    return {"msg":"Removido com sucesso"};

# Filme
@app.post("/filmes",status_code=201)
def criar_filme(filme:schemas.Filme,db:Session=Depends(get_db)) -> dict:
    retorno = RepositorioFilme(db).criar(filme);
    return retorno;

@app.get("/filmes")
def pegar_filmes(db:Session=Depends(get_db)) -> dict:
    retorno = RepositorioFilme(db).listar();
    return retorno;

@app.get("/filmes/{id}")
def pegar_filme(id:int,db:Session=Depends(get_db)) -> dict:
    retorno = RepositorioFilme(db).obter(id);
    return retorno;

@app.get("/filmes/titulo")
def pegar_filme(titulo:Titulo,db:Session=Depends(get_db)) -> dict:
    titulo = titulo.titulo;
    retorno = RepositorioFilme(db).obter_titulo(titulo);
    return retorno;

@app.delete("/filmes/{id}")
def pegar_filme(id:int,db:Session=Depends(get_db)) -> dict:
    RepositorioFilme(db).remover(id);
    return {"msg":"Removido com sucesso"};
#-----------------------
# Main()
#-----------------------
#-----------------------