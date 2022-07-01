"""AppBLX"""
#-----------------------
# BIBLIOTECAS
#-----------------------
import sys
from fastapi import FastAPI
from src.routers import router_pedido
from src.routers import router_produto
from src.routers import router_usuario
from fastapi.middleware.cors import CORSMiddleware
#-----------------------
# Remover __pycache__
#-----------------------
sys.dont_write_bytecode = True;
# sys.dont_write_bytecode = False;
#-----------------------
# FastApi
#-----------------------
app = FastAPI();
#-----------------------
# CORS
#-----------------------
origins = [
    "http://localhost",
    "http://localhost:8000",
];

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
);
#-----------------------
# Routers
#-----------------------
app.include_router(router_pedido.router);
app.include_router(router_produto.router);
app.include_router(router_usuario.router);
#-----------------------