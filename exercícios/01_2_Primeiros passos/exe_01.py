"""
Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no
conteúdo.
"""

frase1 = str(input('Digite a primeira frase: ')).strip().title()
frase2 = str(input('Digite a segunda frase: ')).strip().title()

print(f"\nA Primeira frase tem {len(frase1) - frase1.count(' ')} letras.")
print(f"A Segunda frase tem {len(frase2) - frase2.count(' ')} letras.")

if frase1 == frase2:
    print('\nAs duas frases iguais no tamanho e no conteúdo!')
elif len(frase1) == len(frase2):
    print('\nAs duas frases tem o mesmo tamanho, mas não são iguais.')
else:
    print('\nAs duas frases são diferentes no tamanho e conteúdo!')
