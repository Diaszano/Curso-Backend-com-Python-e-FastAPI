"""Modulo do Server

Neste modulo iremos ter o servidor.
"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from fastapi import FastAPI
from pydantic import BaseModel
#-----------------------
# CONSTANTES
#-----------------------
app = FastAPI();
#-----------------------
# CLASSES
#-----------------------
class Produto(BaseModel):
    nome : str
    preco: float
#-----------------------
# FUNÇÕES()
#-----------------------
@app.get("/")
async def home() -> dict:
    """Home - Método GET
    
    Está é a página inicial do programa e 
    retorna apenas um "Olá Mundo!".
    """
    return {"mensagem":"Olá Mundo!"};

@app.post("/produto")
async def produtos(produto: Produto) -> dict:
    """Produtos - Método POST
    
    Está é a página dos produtos aonde nós 
    iremos cadastrar os produtos.
    """
    return {"mensagem":"Olá Mundo!"};
#-----------------------
# Main()
#-----------------------
#-----------------------