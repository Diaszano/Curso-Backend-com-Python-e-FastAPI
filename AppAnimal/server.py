"""Modulo AppAnimal

Neste modulo iremos resolver o exercício proposto.
"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from enum import Enum
from random import randint
from fastapi import FastAPI
from pydantic import BaseModel, validator, constr
#-----------------------
# CONSTANTES
#-----------------------
app:FastAPI  = FastAPI();
Animais:list = [];
MIN_ID:int   = 1;
MAX_ID:int   = 1000;
#-----------------------
# CLASSES
#-----------------------
class Sexo(Enum):
    """Sexo do Animal
    
    Aqui nós iremos dizer qual é o sexo do animal.

    Para isso nós precisaremos escolher entre:
    \n\tMacho = 1.
    \n\tFêmea = 2.
    """ 
    def __str__(self) -> str:
        return self.name.upper();
    
    def __repr__(self) -> str:
        return f"{self}";
    
    macho = 1;
    femea = 2;

class Animal(BaseModel):
    nome : constr(max_length=60,min_length=1);
    idade: float;
    sexo : Sexo;
    cor  : constr(max_length=20,min_length=1);

    @validator('idade')
    def verificar_idade(cls, idade) -> float:
        if(idade < 0):
            raise ValueError('Idade inexistente');
        return idade;
    
    @validator('sexo')
    def modificar_tipo(cls, sexo) -> str:
        return str(sexo);
#-----------------------
# FUNÇÕES()
#-----------------------
@app.post("/animais")
async def insert(animal:Animal) -> dict:
    """Insert - Método Post
    
    Este é o método aonde vamos fazer a inserção 
    de um animal na API.
    """
    novo_animal:dict = {
        "ID":randint(MIN_ID,MAX_ID),
        "Animal":animal
    };
    Animais.append(novo_animal);
    mensagem:str = (
        f"O animal {animal.nome} "
        "foi cadastrado com sucesso!"
    );
    retorno:dict = {
        "mensagem":f"{mensagem}",
        "Valido":f"{True}"
    }
    return retorno;

@app.get("/animais")
async def listar() -> dict:
    """Listar - Método GET
    
    Este é o método aonde vamos pegar todos os animais 
    salvos na API.
    """
    retorno:dict = {
        "Animais":Animais
    };
    return retorno;

@app.get("/animais/{id}")
async def pegar(id:int) -> dict:
    """Pegar - Método GET
    
    Este é o método aonde vamos pegar o animal com o id 
    salvo na API.
    """
    retorno:dict = {
        "Erro":"Animal inexistente"
    };
    if(id > MAX_ID or id < MIN_ID):
        return retorno;
    for animal in Animais:
        if int(animal["ID"]) == id:
            retorno = {
                "Animal":animal
            }
            return retorno;
    return retorno;

@app.delete("/animais/{id}")
async def deletar(id:int) -> dict:
    """Deletar - Método Delete
    
    Este é o método aonde vamos deletar o animal com o id 
    salvo na API.
    """
    retorno:dict = {
        "Erro":"Animal inexistente"
    };
    if(id > MAX_ID or id < MIN_ID):
        return retorno;
    
    rm = None;
    for animal in Animais:
        if int(animal["ID"]) == id:
            rm = animal
            break;
    if(rm != None):
        Animais.remove(rm);
        retorno = {
            "mensagem":f"O animal {rm['Animal'].nome} removido"
        }
    return retorno;
#-----------------------
# Main()
#-----------------------
#-----------------------