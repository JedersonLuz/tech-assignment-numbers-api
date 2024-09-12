# Tech Assignment - Numbers API

Este repositório contém uma API desenvolvida como parte de um tech assignment. A API possui dois endpoints que realizam cálculos matemáticos utilizando classes desenvolvidas para este propósito.

## Dependências

Para executar esta API, é necessário ter instalado em sua máquina o Python 3.12 e o gerenciador de pacotes Poetry. Para instalar o Poetry, siga as instruções disponíveis em https://python-poetry.org/docs/#installation.

## Endpoints

### Endpoint 1: `/sum`

Este endpoint realiza a soma de dois números. Para utilizá-lo, envie uma requisição HTTP POST para `/soma` com o parâmetro `numbers` contendo a lista de números que deseja somar. A resposta será um JSON contendo o resultado da soma.

Exemplo de requisição:
```
POST /soma
{
  "numbers": [1, 2, 3, 4, 5]
}
```

Exemplo de resposta:
```
{
  "resultado": 15
}
```

### Endpoint 2: `/average`

Este endpoint calcula a média de uma lista de números. Para utilizá-lo, envie uma requisição HTTP POST para `/average` com o parâmetro `numbers` contendo a lista de números que deseja calcular a média. A resposta será um JSON contendo o resultado da média.

Exemplo de requisição:
```
POST /average
{
  "numbers": [1, 2, 3, 4, 5]
}
```

Exemplo de resposta:
```
{
  "resultado": 3
}
```

## Como utilizar a API

Para utilizar esta API, siga os seguintes passos:

1. Clone este repositório em sua máquina local.
2. Instale as dependências necessárias utilizando poetry:
```
poetry install
```
3. Execute a aplicação:
```
fastapi run
```
4. Acesse a documentação da API em `http://localhost:8000/docs` para mais informações sobre os endpoints disponíveis.
5. Para realizar testes unitários, execute o comando:
```
pytest
```
