import csv

dados = [
['Produto', 'Valor'],
['Caixa', '10'],
['Sapato', '15.5'],
['Botão', '32'],
['Sopa', '11.2'],
]

with open('dados2.csv', 'w', encoding='UTF-8', newline='') as arquivo:
    escritor = csv.writer(arquivo)

    for linha in dados:
        escritor.writerow(linha)