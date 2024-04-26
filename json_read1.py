import json

with open('dados.json', 'r', encoding='UTF-8') as arquivo:
    dados = json.load(arquivo)

    for dado in dados:
        print(f'{dado['Produto']} custa R$ {dado['Valor']:.2f}')