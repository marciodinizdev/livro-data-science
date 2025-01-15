'''
Programa que recebe um número inteiro e exibe a tabuada desse número de 1 a 10.
'''

numero = int(input('Digite um número inteiro: '))
print(f'tabuada do {numero}:')
for indice in range(1, 11):
    print(f'{numero} x {indice} = {numero * indice}')