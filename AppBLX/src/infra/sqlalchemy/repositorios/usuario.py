"""Usuários"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy import models
from sqlalchemy import select, update, delete
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class RepositorioUsuario():
    def __init__(self, session:Session) -> None:
        self.session = session;
    
    def criar(self, usuario: schemas.Usuario) -> models.Usuario:
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
    
    def editar(self,id:int,usuario:schemas.Usuario) -> None:
        stmt = update(models.Usuario).where(
            models.Usuario.id==id
        ).values(
            nome     = usuario.nome,
            telefone = usuario.telefone,
            senha    = usuario.senha
        );
        self.session.execute(stmt);
        self.session.commit();
    
    def remover(self,id:int) -> None:
        stmt = delete(models.Usuario).where(
            models.Usuario.id==id
        )
        self.session.execute(stmt);
        self.session.commit();
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------