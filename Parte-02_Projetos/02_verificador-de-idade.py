'''
Programa que pede a idade do usuário e diz se ele é:

1 -> Criança (até 12 anos),
2 -> Adolescente (13 a 17 anos),
3 -> Adulto (18 a 59 anos),
4 -> Idoso (60 anos ou mais).
'''

idade = int(input('Digite sua idade: '))
if idade <= 12:
    print('Você é uma criança.')
elif idade >= 13 and idade <= 17:
    print('Você é um adolescente.')
elif idade >= 18 and idade <= 59:
    print('Você é um adulto.')
else:
    print('Você é um idoso.')