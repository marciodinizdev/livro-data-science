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

