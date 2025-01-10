#1
print('\nNúmeros pares divisíveis por 4 e 3 entre 2000 e 5000:')
for x in range(2000, 5000, 2):
    if(x % 4 == 0 and x % 3 == 0):
        print(x, end=' ')

#2
print('\nListando números pares divisíveis por 4 e 3 entre 2000 e 5000 e multiplicando-os por 1.5:')
for x in range(2000, 5000, 2):
    if(x % 4 == 0 and x % 3 == 0):
        print(x * 1.5, end=' ')

#3
print('Crivo de Eratóstenes para encontrar números primos entre 0 e 100:')

import math

numeros = []
for i in range(101):
    numeros.append(True)
i = 2
while(i <= int(math.sqrt(100))):
    if numeros[i]:
        for j in range(i*2, 101, i):
            numeros[j]=False
    i = i+1
for i in range(2,101):
  if numeros[i]:
      print(i)