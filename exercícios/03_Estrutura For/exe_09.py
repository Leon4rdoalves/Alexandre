"""
 Faça um programa que leia ano de nascimento de 5 pessoas e no final
 mostra quantas pessoas já atingiram a maior idade e para aquelas que
 ainda atingiram, mostre a média em anos que faltam para chegarem a maior idade.
"""

# from datetime import date
# ano_atual = date.today().year

ano_atual = 2020
maior_idd = cont_menor = soma_menor = 0

for cont in range(3):
    ano = int(input('Digite seu ano de nascimento: '))

    if (ano_atual - ano) >= 18:
        maior_idd += 1

    if (ano_atual - ano) < 18:
        cont_menor += 1
        soma_menor += 18 - (ano_atual - ano)

media_menor = soma_menor / cont_menor

print(f'\nTotal de pessoas com maioridade: {maior_idd}')
print(f'Total de pessoas menores de idade: {cont_menor}')
print(f'Total em anos que faltam para todos completarem 18 anos: {soma_menor}')
print(f'Média de anos que faltam para atingir 18 anos: {media_menor:.2f}')
