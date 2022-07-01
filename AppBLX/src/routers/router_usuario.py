""""""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
#-----------------------
# CONSTANTES
#-----------------------
router = APIRouter();
NOME_TAG = "Usuários";
#-----------------------
# CLASSES
#-----------------------
#-----------------------
# FUNÇÕES()
#-----------------------
@router.get(  "/usuarios",
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.Usuario],
            tags=[NOME_TAG]
        )
def listar_usuarios(session:Session=Depends(get_db)):
    lista_produtos = RepositorioUsuario(session).listar();
    return lista_produtos;

@router.post(  "/usuarios",
            status_code=status.HTTP_201_CREATED,
            response_model=schemas.Usuario,
            tags=[NOME_TAG]
        )
def criar_usuarios(produto:schemas.Usuario,session:Session=Depends(get_db)):
    produto_criado = RepositorioUsuario(session).criar(produto);
    return produto_criado;
#-----------------------
# Main()
#-----------------------
#-----------------------