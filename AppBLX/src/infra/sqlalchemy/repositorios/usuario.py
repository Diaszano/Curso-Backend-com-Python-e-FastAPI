"""Usuários"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy import models
from sqlalchemy import select, update, delete, insert
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class RepositorioUsuario():
    def __init__(self, session:Session) -> None:
        self.session = session;
    
    def criarRetorno(self, usuario: schemas.Usuario) -> models.Usuario:
        session_usuario = models.Usuario(
            nome     = usuario.nome,
            telefone = usuario.telefone,
            senha    = usuario.senha
        );
        
        self.session.add(session_usuario);
        self.session.commit();
        self.session.refresh(session_usuario);
        return session_usuario;
    
    def criar(self, usuario: schemas.Usuario) -> None:
        stmt = insert(models.Usuario).values(
            nome     = usuario.nome,
            telefone = usuario.telefone,
            senha    = usuario.senha
        );
        self.session.execute(stmt);
        self.session.commit();
    
    def listar(self) -> List[models.Usuario]:
        stmt = select(models.Usuario);
        usuarios = self.session.execute(stmt).scalars().all();
        return usuarios;
    
    def editar(self,idUser:int,usuario:schemas.Usuario) -> None:
        stmt = update(models.Usuario).where(
            models.Usuario.id==idUser
        ).values(
            nome     = usuario.nome,
            telefone = usuario.telefone,
            senha    = usuario.senha
        );
        self.session.execute(stmt);
        self.session.commit();
    
    def remover(self,idUser:int) -> None:
        stmt = delete(models.Usuario).where(
            models.Usuario.id==idUser
        )
        self.session.execute(stmt);
        self.session.commit();
    
    def obter_pelo_telefone(self,telefone:str) -> models.Usuario:
        stmt = select(models.Usuario).where(
            models.Usuario.telefone == telefone
        );
        retorno =  self.session.execute(stmt).scalars().first();
        return retorno;
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------