"""Usuários"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from sqlalchemy import select
from AppBLX.src.schemas import usuario
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class RepositorioUsuario():
    def __init__(self, session:Session) -> None:
        self.session = session;
    
    def criar(self, usuario: usuario.Usuario) -> models.Usuario:
        session_usuario = models.Usuario(
            nome     = usuario.nome,
            telefone = usuario.telefone,
            senha    = usuario.senha
        );

        self.session.add(session_usuario);
        self.session.commit();
        self.session.refresh(session_usuario);
        return session_usuario;
    
    def listar(self) -> List[models.Usuario]:
        stmt = select(models.Usuario);
        usuarios = self.session.execute(stmt).scalars().all();
        return usuarios;
    
    def obter(self) -> None:
        pass;
    
    def remover(self) -> None:
        pass;
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------