# O if testa condições e se elas forem satisfeitas executa o código de um suíte identado

# Dada a variável
x = 5

print('Testando x...')
if x > 0: # testa se x > 0
    print(f'{x} é um número positivo') # Código executado caso o if for satisfeito
print('Linha fora da identação. Será executada independente do if.')

y = -1
print('Testando y...')
if y > 0:
    print(f'{y} é um número positivo') # y não é maior que 0, portanto esse código não será executado
print('Linha fora da identação. Será executada independente do if.')
