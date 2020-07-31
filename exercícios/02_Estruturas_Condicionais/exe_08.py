"""
Faça um programa que peça o preço de 3 produtos e informe ao usuário qual produto
ele deve comprar, sendo que, o usuário deseja comprar aquele que for mais barato.
"""
'''
arroz = float(input('Digite o valor do Arroz: '))
feijao = float(input('Digite o valor do Feijão: '))
batata = float(input('Digite o valor da batata: '))

if batata < feijao and batata < arroz:
    print(f'\nVocê deve comprar batata.')
if feijao < arroz and feijao < batata:
    print(f'\nVocê deve comprar feijão.')
if arroz < feijao and arroz < batata:
    print(f'\nVocê deve comprar arroz.')
'''


produto1 = str(input('Digite o produto: '))
valor1 = float(input(f'Digite o valor do(a) {produto1}: '))
produto2 = str(input('Digite o produto: '))
valor2 = float(input(f'Digite o valor do(a) {produto2}: '))
produto3 = str(input('Digite o produto: '))
valor3 = float(input(f'Digite o valor do(a) {produto3}: '))


n_maisbarato = produto1
v_maisbarato = valor1

if valor2 < valor1 and valor2 < valor3:
    n_maisbarato = produto2
    v_maisbarato = valor2


if valor3 < valor1 and valor3 < valor2:
    v_maisbarato = valor3
    n_maisbarato = produto3


print(f'\nCom valor R${v_maisbarato:.2f} o produto a ser comprado é: {n_maisbarato}')
