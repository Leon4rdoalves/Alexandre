"""
Faça um programa cadastro. Ele deve solicitar o nome, idade e sexo de 10 pessoas.
Ao final mostre, a média de idade de todos dos homens e das mulheres,
assim como a média geral. O nome do homem mais velho e da mulher mais nova.
Obrigatório utilizar estrutura FOR.
"""

maior = menor = soma_id_h = cont_h = soma_id_m = cont_m = cont_g = soma_id_g = 0
nome_velho = ''
nome_nova = ''

for cont in range(5):
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M | F]: ')).strip().upper()
    print('*' * 35)

    soma_id_g += idade
    cont_g += 1

    if cont == 0:
        maior = idade
        menor = idade

    if sexo == 'M':
        soma_id_h += idade
        cont_h += 1
        if idade > maior:
            maior = idade
            nome_velho = nome

    elif sexo == 'F':
        soma_id_h += idade
        cont_m += 1
        if idade < menor:
            menor = idade
            nome_nova = nome
    else:
        print('Dado inválido!!!')

media_m = soma_id_m / cont_m
media_h = soma_id_h / cont_h
media_g = soma_id_g / cont_g


print(f'Média de idade dos homens cadastrados: {media_h:.2f}')
