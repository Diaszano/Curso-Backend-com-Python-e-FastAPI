""""""
#-----------------------
# BIBLIOTECAS
#-----------------------
from jose import JWTError
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.providers import token_provider
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
#-----------------------
# CONSTANTES
#-----------------------
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token");
#-----------------------
# CLASSES
#-----------------------
#-----------------------
# FUNÇÕES()
#-----------------------
def obter_usuario_logado(token:str=Depends(oauth2_scheme),session:Session=Depends(get_db)) -> schemas.Usuario:
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido"
    );

    try:
        telefone = token_provider.verificar_access_token(token);
    except JWTError:
        raise exception;
    
    if(not telefone):
        raise exception;
    
    usuario = RepositorioUsuario(session).obter_pelo_telefone(telefone);
    
    if(not usuario):
        raise exception;
    
    return usuario;
#-----------------------
# Main()
#-----------------------
#-----------------------