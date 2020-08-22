"""
Faça um programa que mostre na tela uma contagem de 1 a 50.
Utilizando a estrutura FOR.
"""

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo:'))

if inicio > fim and passo < 0:
    for c in range(fim, inicio - 1, passo):
        print(c)

elif inicio < fim and passo > 0:
    for c in range(inicio, fim + 1, passo):
        print(c)

else:
    print('Não foi possível executar com o passo informado.')


