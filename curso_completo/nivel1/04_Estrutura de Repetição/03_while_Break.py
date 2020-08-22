"""
While com Break

while True: >>> este laço será executado enquanto não encontrar o Break pelo caminho.

Break >>> Condição de parada de um loop.

"""
'''
cont = 0

while cont <= 10:
    print(cont)
    cont += 1



while True:
    nome = str(input('Digite Nome ou Sair para encerrar: ')).title().strip()
    
    
    if nome != 'Sair':
        print(f'Muito prazer, {nome}')
        
    else:
        break
'''


senha = '123456'

while True:
    entrada = str(input('Digite sua senha: '))

    if entrada != senha:
        print('\033[31mAcesso negado... tente novamente!\033[m\n')
    else:
        print('Abrindo a próxima janela...')
        break
