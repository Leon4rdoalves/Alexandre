"""
ESTRUTURA DE REPETIÇÃO

For >>> Utilizada quando se sabe a quantidade de repetições que serão necessárias, de forma que é
obrigatório determinar o final da execução do laço.

Sintaxe >>> for item in iteravel:
                execução

* Range
    Ex. Contador 10 - 0
                 0 - 10
                  step

* Enumerate
     Ex. for valor in enumerate(frase)

"""

# Exemplo 1

'''taxa = 0.1

valor = float(input('Digite o valor inicial: '))
mes = int(input('Em quantos meses deseja fazer a retirada: '))

for cont in range(mes):
    calc = valor * taxa
    if cont == 0:
        print(f'\nValor inicial mês {cont}: R${valor:.2f}')

    valor += calc

    print(f'Retirada no {cont + 1}º mês: R${valor:.2f}')'''

# Exemplo 2
'''
frase = 'Python é vida dfgdfg dfg fdgdf g dfg dfg dfg dfg dfg '
frase1 = 'Python é vida'

for f in enumerate(frase):
    print(f)

print()

for f1 in enumerate(frase1):
    print(f1)'''

# Exemplo 3
'''
palavras = ['Leonardo', 'Alves', 'Batata', 'suco de fruta']

for palavra in palavras:
    print(palavra)
'''

# Exemplo 4

palavra = 'Leonardo'

for letra in palavra:
    print(letra)

