"""Filme"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from typing import List
from src.schemas import schemas
from sqlalchemy.orm import Session
from sqlalchemy import select, delete
from src.infra.sqlalchemy.models import models
#-----------------------
# CONSTANTES/GLOBAIS
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class RepositorioFilme():
    def __init__(self, db:Session) -> None:
        self.db = db;
    
    def criar(self, filme: schemas.Filme) -> models.Filme:
        db_filmes = models.Filme(
            titulo         = filme.titulo,
            ano            = filme.ano,
            sinopse        = filme.sinopse,
        )

        self.db.add(db_filmes);
        self.db.commit();
        self.db.refresh(db_filmes);
        return db_filmes;
    
    def listar(self) -> List[models.Filme]:
        filmes = self.db.query(models.Filme).all();
        return filmes;
    
    def obter(self, filmes_id:int) -> models.Filme:
        stmt = select(models.Filme).filter_by(
            id=filmes_id
        );
        filme = self.db.execute(stmt).one();
        return filme;
    
    def obter_titulo(self, filme_titulo:str) -> models.Filme:
        stmt = self.db.query(models.Filme).filter(
            models.Filme.titulo.like(f"{filme_titulo}%")
        );
        filmes = self.db.execute(stmt).all();
        return filmes;
        
    def remover(self, filmes_id:int) -> None:
        stmt = delete(models.Filme).where(
            models.Filme.id == filmes_id
        )
        self.db.execute(stmt);
        self.db.commit();
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------