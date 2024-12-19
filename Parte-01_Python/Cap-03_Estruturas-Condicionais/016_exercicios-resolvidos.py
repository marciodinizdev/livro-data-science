#1
var1 = 11
var2 = 23
var3 = 3

print('Verificando qual é o maior número...')
if var1 > var2 and var1 > var3: # var1 é maior que todos?
    print('O maior é:', var1)
elif var2 > var1 and var2 > var3: # var2 é maior que todos?
    print('O maior é:', var2)
else:
    print('O maior é:', var3)

#2
import random
print('Gerando um número aleatório entre -100 e 100...')
numero_aleatorio = random.randint(-100, 100)
if (numero_aleatorio > 0):
    print(f'O número {numero_aleatorio} é MAIOR que 0.')
elif (numero_aleatorio < 0):
    print(f'O número {numero_aleatorio} é MENOR que 0.')
else:
    print(f'O número {numero_aleatorio} é 0.')