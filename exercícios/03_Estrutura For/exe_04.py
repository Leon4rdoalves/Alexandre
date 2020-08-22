"""
Faça um programa Tabuada,
que permite ao usuário informar o número a ser multiplicado.
"""

num = int(input('Digite um número para criar a tabuada: '))
print()
for cont in range(1, 11):
    print(f'{num} X {cont} = {num * cont}')
