"""
Faça um programa que leia 5 números e ao final,
mostre o maior e menor número digitado.
"""

maior = menor = 0

for n in range(5):
    num = int(input(f'Digite o {n + 1}º número: '))

    if n == 0:
        maior = num
        menor = num

    if num > maior:
        maior = num

    if num < menor:
        menor = num