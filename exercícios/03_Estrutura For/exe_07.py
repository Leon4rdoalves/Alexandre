"""
Faça um programa que leia um número inteiro e na sequencia mostre se ele é ou não um número primo.
(Números primos são divisíveis por 1 e eles mesmos apenas).
"""

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):

    if num % c == 0:
        print('\33[31m', end=' ')
        tot += 1
    else:
        print('\33[33m', end=' ')

    print(f'{c}', end=' ')

print(f'\nO número {num} é divisível {tot} vezes')

if tot == 2:
    print('Por isso o número é primo!')
else:
    print('Por isso o número Não é primo!')

