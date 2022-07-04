"""AppBLX"""
#-----------------------
# BIBLIOTECAS
#-----------------------
from fastapi import FastAPI
from src.routers import router_auth
from src.routers import router_pedido
from src.routers import router_produto
from fastapi.middleware.cors import CORSMiddleware
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
app.include_router(router_pedido.router,prefix="/pedidos");
app.include_router(router_produto.router,prefix="/produtos");
app.include_router(router_auth.router,prefix="/auth");
#-----------------------