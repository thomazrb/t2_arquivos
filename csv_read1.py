with open('dados.csv', 'r', encoding='UTF-8') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        lista = linha.split(',')
        print(lista)
        produto, valor = lista
        print(produto)
        print(valor)

