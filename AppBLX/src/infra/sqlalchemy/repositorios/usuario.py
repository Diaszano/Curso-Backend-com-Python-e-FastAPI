"""Modulo Models"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
#-----------------------
# CONSTANTES
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class RepositorioUsuario():
    def __init__(self, db:Session) -> None:
        self.db = db;
    
    def criar(self, usuario: schemas.Usuario) -> models.Usuario:
        db_usuario = models.Usuario(
            nome=usuario.nome,
            telefone=usuario.telefone
        );

        self.db.add(db_usuario);
        self.db.commit();
        self.db.refresh(db_usuario);
        return db_usuario;
    
    def listar(self) -> List[models.Usuario]:
        usuarios = self.db.query(models.Usuario).all();
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