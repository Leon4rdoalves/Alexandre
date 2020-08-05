"""
Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

"""

st1 = input('Digite String 1:')
st2 = input('Digite String 2:')

lenghtst1 = len(st1)
lenghtst2 = len(st2)

print(f'A String 1 contém {lenghtst1} caracteres!')
print(f'A String 2 contém {lenghtst2} caracteres!')

if lenghtst1 == lenghtst2:
    print('Sim, o comprimento das duas strings são iguais')
else:
    print('Não, o comprimento das duas strings são diferentes')

