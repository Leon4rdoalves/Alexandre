"""
ESTRUTURAS LÓGICAS E CONDICIONAIS

If, Else, Elif >>> Extrutura condicional, permite que o código trafegue por vários caminhos, de acordo com a decisões
que são tomadas no decorrer da execução. Ps. Elif só existem em Python

Em Python:

Condições Simples >>> Teste sim ou não.
Condições Compostas >>> Teste 2 ou mais expressões.
Condições Aninhadas >>> Teste condições dentro de outras condições.

Ex. Habilitação 18/16/Autorização"""

idade = int(input('Digite sua idade: '))

if (idade >= 16) and (idade < 18):
    conf = str(input('Vc tem autorização: [S / N]: ')).lower()

    if conf == 's':
        conf1 = str(input('Posso confiar?'))

        if conf1 == 's':
            print('Ok, seu processo foi iniciado')


    else:
        print('Vá buscar a autorização!')


elif idade >= 18:
    print('Vc está apto à tirar sua CNH.')


else:
    print('Vc não tem idade para tirar sua CNH.')

print('\nSistema finalizado')
