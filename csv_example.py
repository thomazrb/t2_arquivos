import csv

with open('dados2.csv', mode='r', encoding='UTF-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    linhas = list(leitor_csv)

 
for i, linha in enumerate(linhas):
    if linha[0] == 'Sapato':
        linhas[i][1] = '16'

with open('dados2.csv', mode='w', encoding='UTF-8', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    for linha in linhas:
        escritor_csv.writerow(linha)
        