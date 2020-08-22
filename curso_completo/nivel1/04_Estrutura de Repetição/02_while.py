"""
While >>> Utilizada quando se sabe a quantidade de repetições e quando não se sabe.
* Necessário atentar para o critério de parada.

Sintaxe >>>  while expressão_bool:
                    Execução.

Expressão será executada enquanto for verdadeira.
Expressão Booleana >>> Toda expressão onde o resultado for Verdadeiro ou Falso.

Ex.
resposta = ''
    while resposta != 'SIM':
        resposta = input
"""
'''
for cont in range(11):
    print(cont)
print('finalizei...')


cont = 0
while cont <= 10:
    print(cont)
    cont += 1
print('terminei...')

resposta = ''

while resposta != 'sair':
    resposta = str(input('Para encerrar, digite sair: '))


print('\nOk, programa finalizado.')


# forçar uma entrada de texto.

nome = ''

while not nome.isnumeric():
    nome = input('Nome: ')

    if not nome.isnumeric():
        print(f'Muito prazer, {nome}!\n')

    else:
        print('Ops, dado inválido!')
'''