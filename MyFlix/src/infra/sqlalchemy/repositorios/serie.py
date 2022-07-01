"""Serie"""
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
class RepositorioSerie():
    def __init__(self, db:Session) -> None:
        self.db = db;
    
    def criar(self, serie: schemas.Serie) -> models.Serie:
        db_serie = models.Serie(
            titulo         = serie.titulo,
            ano            = serie.ano,
            sinopse        = serie.sinopse,
            qtd_temporadas = serie.qtd_temporadas
        )

        self.db.add(db_serie);
        self.db.commit();
        self.db.refresh(db_serie);
        return db_serie;
    
    def listar(self) -> List[models.Serie]:
        series = self.db.query(models.Serie).all();
        return series;
    
    def obter(self, serie_id:int) -> models.Serie:
        stmt = select(models.Serie).filter_by(
            id=serie_id
        );
        serie = self.db.execute(stmt).one();
        return serie;
    
    def obter_titulo(self, serie_titulo:str) -> models.Serie:
        stmt = self.db.query(models.Serie).filter(
            models.Serie.titulo.like(f"{serie_titulo}%")
        );
        series = self.db.execute(stmt).all();
        return series;
        
    def remover(self, serie_id:int) -> None:
        stmt = delete(models.Serie).where(
            models.Serie.id == serie_id
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