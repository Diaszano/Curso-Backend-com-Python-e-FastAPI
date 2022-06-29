# 🐍 AppBLX - Sistema de anúncios e vendas de produtos na vizinhança

## Funcionalidades:

- Qualquer pessoa poderá anunciar produtos.
- Qualquer pessoa poderá fazer pedidos dos produtos anunciados.
- Uma pessoa tem:
    - Nome
    - Telefone whatsapp
    - senha
- Um produto tem:
    - Nome
    - Detalhes
    - Preço
    - Disponível
    - Fotos
- Um pedido tem:
    - Produto
    - Pessoa que está pedindo
    - Quantidade
    - Local de entrega
    - Observações
    - Entrega ou Retirada
- Cada usuário terá uma lista de pedidos recebidos e pedidos feitos.
- O pedido deverá ser aceito pelo vendedor
- O comprador poderá acompanhar seus pedidos:
    - Status (Feito,Aceito)

## Arquitetura e Ferramentas

- [Utilizamos a linguagem Python](https://www.python.org/)
- [Utilizamos FastAPI](https://fastapi.tiangolo.com/)
- Banco de Dados:
    - [PostgreSQL](https://www.postgresql.org/)
    - [MongoDB](https://www.mongodb.com/pt-br)
    - [Firebase](https://firebase.google.com/)
- Docker para o Banco de Dados
- MVC
- DDD e Arquitetura Limpa
