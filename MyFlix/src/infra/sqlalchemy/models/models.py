"""Models"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from sqlalchemy import Column, Integer, String
from src.infra.sqlalchemy.config.database import Base
#-----------------------
# CONSTANTES/GLOBAIS
#-----------------------
#-----------------------
# CLASSES
#-----------------------
class Serie(Base):
    """Série - Models
    
    Neste modelo nós criamos a tabela das séries.
    """
    __tablename__ = "serie";

    id = Column(
        Integer,
        primary_key=True,
        index=True
    );
    titulo         = Column(String);
    ano            = Column(Integer);
    sinopse        = Column(String);
    qtd_temporadas = Column(Integer);

class Filme(Base):
    """Filme - Models
    
    Neste modelo nós criamos a tabela das filmes.
    """
    __tablename__ = "filme";

    id = Column(
        Integer,
        primary_key=True,
        index=True
    );
    titulo         = Column(String);
    ano            = Column(Integer);
    sinopse        = Column(String);
#-----------------------
# FUNÇÕES()
#-----------------------
#-----------------------
# Main()
#-----------------------
#-----------------------