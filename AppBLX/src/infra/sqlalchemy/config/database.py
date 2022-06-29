"""DataBase"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#-----------------------
# CONSTANTES - GLOBAIS
#-----------------------
SQLALCHEMY_DATABASE_URL:str = (
    "sqlite:///./app_blx.db"
    # "postgresql://user:password@postgresserver/db"
);
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args = {
        "check_same_thread": False
        }
);
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
);
Base = declarative_base();
#-----------------------
# CLASSES
#-----------------------
#-----------------------
# FUNÇÕES()
#-----------------------
def criar_db() -> None:
    """Criação do Banco de Dados
    
    Nesta função nós iremos fazer a 
    criação do banco de dados.
    """
    Base.metadata.create_all(
        bind=engine
    );

def get_db() -> sessionmaker:
    """Pegar a Conexão
    
    Nesta função nós iremos fazer a 
    conexão com o banco de dados.
    """
    db = SessionLocal();
    try:
        yield db;
    finally:
        db.close();
#-----------------------
# Main()
#-----------------------
#-----------------------
