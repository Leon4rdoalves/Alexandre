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

a = str(input('\n\033[mEsteve no local do crime? ')).strip().lower()
b = str(input('Devia para a vítima? ')).strip().lower()
c = str(input('Mora perto da vítima? ')).strip().lower()
d = str(input('Já trabalhou com a vitíma? ')).strip().lower()
e = str(input('Telefonou para a vítima: ')).strip().lower()
f = str(input('Está tenso? ')).strip().lower()

if a == 's' and b == 's' and c == 's' and d == 's' and e == 's' and f == 's':
    status = 6
elif a == 's' and b == 's' and c == 's' and d == 's' and e == 's':
    status = 5
elif a == 's' and b == 's' and c == 's' and d == 's':
    status = 4
elif a == 's' and b == 's' and c == 's':
    status = 3
elif a == 's' and b == 's':
    status = 2
elif a == 's':
    status = 1
else:
    status = 0

if (status > 0) and (status <= 2):
    resp = 'Suspeito!'
elif (status >= 3) and (status <= 4):
    resp = 'Cúmplice!'
elif (status >= 5) and (status <= 6):
    resp = 'Assassino!'
else:
    resp = 'Inocente.'

print(status)
print(resp)
