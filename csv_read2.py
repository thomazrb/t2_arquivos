import csv

with open('dados.csv', 'r', encoding='UTF-8') as arquivo:

    dados = csv.reader(arquivo)

    for dado in dados:
        produto, valor = dado
        print(produto)
        print(valor)