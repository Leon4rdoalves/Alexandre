"""
 Faça um programa que identifique se uma frase é não palíndromo.
"""


frase = str(input('Digite uma frase: '))

palavras = (frase.split())

juntas = ''.join(palavras)

invertido = ''

for letra in range(len(juntas)-1, -1, -1):
    invertido += juntas[letra]

# print(invertido)

if invertido == juntas:
    print('\nLegal, a frase que você digitou é um palíndromo!')
else:
    print('\nOps, analisei aqui e esta frase não é um palíndromo!!!')
