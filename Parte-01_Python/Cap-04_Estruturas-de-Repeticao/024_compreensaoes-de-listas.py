### Especificando precisamente listas em conjuntos algébricos
print('Entendendo List Comprehensions:')

# Imprimindo uma lista c1 formada por um conjunto de números de 0 até 3 elevados ao cubo
print('C1 = {x³ | 0<=x<=3}')
c1 = [x**3 for x in range(4)]
print(c1)

# Imprimindo uma lista c2 formada por um conjunto de números de 0 até 20 sendo todos pares
print('x | 0<=x<=20 e x é par')
c2 = [x * 2 for x in range(0, 11)] # produz o mesmo que [x for x in range(0, 21, 2)]
print(c2)

# Imprimindo uma lista c2 formada por um conjunto de números de -20 até 40 sendo todos ímpares
print('x | -20<=x<=40 e x é ímpar')
c3 = [x * 2 + 1 for x in range(-10, 20)]
print(c3, sep='')

### É comum usar _ quando não for preciso usar o valor de uma variável de uma lista

# Exemplo: primos = [False for _ in numeros]

### É possível usar loops aninhados com List Comprehensions
numeros = [
    (p1, p2) 
    for p1 in range(7)
    for p2 in range(7)
]
print(f'Pares criados: {numeros}', sep='')