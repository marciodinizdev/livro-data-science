#1
print('\nNúmeros entre 5000 e 10000 divisíveis por 3 e por 7...')
for x in range(5000, 10000):
    if x % 7 == 0 and x % 3 == 0:
        print(x, end=' ')

#2
print('\n\nMesmo resultado mas usando while...')
x = 5000
while x < 10000:
    if ( x % 7 == 0 and x % 3 == 0):
        print(x, end=' ')
    
    x = x + 1
