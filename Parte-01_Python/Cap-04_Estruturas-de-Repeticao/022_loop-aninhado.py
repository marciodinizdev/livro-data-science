### Loops aninhados são loops dentro de loops

# Loop aninhado para testar todas as combinações de salas possíveis contendo um número e uma letra
numeros = ['1', '2', '3']
letras = ['a', 'b', 'c']
numero = 0
letra = 0
for numero in range(3):
    for letra in range(3):
        print(f'As salas são: {numeros[numero]}{letras[letra]}')