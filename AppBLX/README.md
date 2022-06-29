# 🐍 AppAnimal - Sistema de cadastro de Animais domésticos

## Descrição:

Faça uma API para operações de cadastro de animais com os seguintes atributos:

- ID   : Gerado randomicamente.
- Nome : Texto.
- Idade: Inteiro.
- Sexo : Macho ou Fêmea.
- Cor  : Texto

## Rotas:

- Post  : Animais       -> Deve enviar um objeto animal com todos os dados exceto id.
- Get   : Animais       -> Deve retornar todos os animais cadastrados.
- Get   : Animais/{id}  -> Deve retornar o animal com o ID especificado.
- Delete: Animais/{id}  -> Apaga o animal com o id especificado.

## Dicas:

- Armazene os dados numa List.
- Use o [Insomnia](https://insomnia.rest/download) para interagir com a sua API.