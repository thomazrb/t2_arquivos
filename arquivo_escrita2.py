try:
    with open('teste.txt', 'x') as arquivo:
        arquivo.write('Teste!\n')
except FileExistsError:
    opcao = input('O arquivo ja existe, quer sobrescrever? (s/n): ')
    if opcao == 's':
        with open('teste.txt', 'w') as arquivo:
            arquivo.write('Teste!\n')
