with open("teste.jpg", 'br') as arquivo:
    dados = arquivo.read()

with open("teste2.jpg", "bw") as arquivo:
    arquivo.write(dados)
