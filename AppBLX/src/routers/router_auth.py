""""""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.providers import hash_provider
from src.infra.sqlalchemy.config.database import get_db
from fastapi import APIRouter, Depends, status, HTTPException
from src.routers.router_auth_utils import obter_usuario_logado
from src.infra.providers.token_provider import create_access_token
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
#-----------------------
# CONSTANTES
#-----------------------
router = APIRouter();
NOME_TAG = "Auth";
#-----------------------
# CLASSES
#-----------------------
#-----------------------
# FUNÇÕES()
#-----------------------
@router.post(  "/signup",
                status_code=status.HTTP_201_CREATED,
                response_model=schemas.UsuarioSimples,
                tags=[NOME_TAG]
            )
async def signup(   usuario:schemas.Usuario,
                    session:Session=Depends(get_db)):
    
    verificar = RepositorioUsuario(session).obter_pelo_telefone(
        usuario.telefone
    );

    if(verificar):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Número de telefone já existente para um usuário!"
        );
    
    usuario.senha = hash_provider.gerar_hash(usuario.senha);

    RepositorioUsuario(session).criar(usuario);

    return usuario;

@router.post(  "/token",
                status_code=status.HTTP_200_OK,
                response_model=schemas.LoginSucesso,
                tags=[NOME_TAG]
            )
async def login(login_data:schemas.LoginData,
                session:Session=Depends(get_db)):
    
    senha    = login_data.senha;
    telefone = login_data.telefone;

    usuario = RepositorioUsuario(session).obter_pelo_telefone(telefone);
    if(not usuario):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Não existe usuário com o telefone {telefone}"
        );
    verificar_senha = hash_provider.verificar_hash(
        senha,
        usuario.senha
    );
    if(not verificar_senha):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Senha incorreta"
        );
    dicionario = {"sub": usuario.telefone};
    token = create_access_token(dicionario);
    retorno = {
        "usuario":usuario,
        "access_token":token
    };
    return retorno;

@router.get(  "/me",
                status_code=status.HTTP_200_OK,
                response_model=schemas.UsuarioSimples,
                tags=[NOME_TAG]
            )
def me(usuario:schemas.Usuario=Depends(obter_usuario_logado)):
    return usuario;
#-----------------------
# Main()
#-----------------------
#-----------------------