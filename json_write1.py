import json

dados = [
    {
        "Produto": "Caixa",
        "Valor": 10
    },
    {
        "Produto": "Sapato",
        "Valor": 15.5
    },
    {
        "Produto": "Botão",
        "Valor": 32
    },
    {
        "Produto": "Sopa",
        "Valor": 11.2
    }
]

with open('dados2.json', 'w', encoding='UTF-8') as arquivo:
    json.dump(dados, arquivo, indent=2, ensure_ascii=False)

