""""""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from fastapi import APIRouter, Depends, status, HTTPException
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
async def listar_usuarios(session:Session=Depends(get_db)):
    lista_usuarios = RepositorioUsuario(session).listar();
    return lista_usuarios;

@router.post(  "/usuarios",
            status_code=status.HTTP_201_CREATED,
            tags=[NOME_TAG]
        )
async def criar_usuarios(usuario:schemas.Usuario,session:Session=Depends(get_db)):
    verificar = RepositorioUsuario(session).verificar_telefone(
        usuario.telefone
    );
    if(verificar):
        raise HTTPException(
            status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
            detail=f"Número de telefone já existente!"
        );
    usuario_criado = RepositorioUsuario(session).criar(usuario);
    return usuario_criado;
#-----------------------
# Main()
#-----------------------
#-----------------------