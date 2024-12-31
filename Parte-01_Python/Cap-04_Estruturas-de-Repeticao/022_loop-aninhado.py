### Loops aninhados são loops dentro de loops

# Loop aninhado para testar todas as combinações de salas possíveis contendo um número e uma letra
numeros = ['1', '2', '3']
letras = ['a', 'b', 'c']
numero = 0
letra = 0
for numero in range(3):
    for letra in range(3):
        print(f'As salas são: {numeros[numero]}{letras[letra]}')

# Loop aninhado para testar todas as magias resultantes de combinações elementais de um jogo incluindo condicionais
elementos_primarios = ['Fogo', 'Água']
elementos_secundarios = ['Terra', 'Vento']

elemento_1 = 0
elemento_2 = 0

for elemento_1 in range(2):
    for elemento_2 in range(2):
        print(f'Você combinou os elementos {elementos_primarios[elemento_1]} e {elementos_secundarios[elemento_2]}')

# O código acima pode ser reescrito como
elementos_primarios = ['Fogo', 'Água']
elementos_secundarios = ['Terra', 'Vento']

elemento_1 = 0
elemento_2 = 0

for elemento_1 in elementos_primarios:
    for elemento_2 in elementos_secundarios:
        print(f'Você combinou os elementos {elemento_1} e {elemento_2}')