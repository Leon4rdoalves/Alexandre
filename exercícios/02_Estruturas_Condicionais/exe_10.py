"""
Faça um programa Detetive. O programa deve perguntar:
a. Esteve no local do crime?
b. Devia para a vítima?
c. Mora perto da vítima?
d. Já trabalhou com a vítima?
e. Telefonou para a vítima?
f. Está tenso?
Pós perguntas, o programa deve mostrar o grau de participação do usuário no crime.
Se a pessoa responder: Se a pessoa responder sim em 2 questões, ela deve ser classificada
como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 ou 6 como “Assassina”.
"""
from time import sleep

print('*' * 60)
print('PROGRAMA DETETIVE'.center(60))
print('*' * 60)
sleep(1)
print('\n\033[32m', '...por favor, aguarde. Instruções sendo carregadas...'.center(60), '\033[m')
sleep(3)
print('\033[1;31m\n', 'ATENÇÃO'.center(60), '\033[m')
print('''
Responda as perguntas apenas com: S para sim ou N para não.
Qualquer resposta diferente destas citadas acima, anulará 
imediatamente o teste.'''.center(60))
sleep(3)
print('\n\033[34m', '...Carregando perguntas...'.center(60), '\033[m')


sleep(6)
a = str(input('\n\033[mEsteve no local do crime? ')).strip().lower()
b = str(input('Devia para a vítima? ')).strip().lower()
c = str(input('Mora perto da vítima? ')).strip().lower()
d = str(input('Já trabalhou com a vitíma? ')).strip().lower()
e = str(input('Telefonou para a vítima: ')).strip().lower()
f = str(input('Está tenso? ')).strip().lower()


