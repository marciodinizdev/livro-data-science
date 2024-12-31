### Break e Continue são instruções usadas para alterar o comportamento de um loop durante sua execução

# Usando break
x = 0
while x < 10:
    x = x + 1
    if(x==5):
        break # encerra o programa imediatamente
    print(f'x = {x}')
print('O programa terminou!')

# Podemos reescrever o exemplo de 019_do-while.py
continua = 's'
somatorio = 0.0
quantidade = 0
while True:
    preco = float(input('Entre com o preço do próximo produto: '))
    somatorio = somatorio + preco
    continua = input('Acrescentar mais produtos? (s/n) ')
    if continua != 's':
        break
print('O valor total dos produtos é R$ %.2f' %somatorio)

# Usando continue
while True:
    letra = input('Digite uma letra diferente de X (Q para sair) ')
    if letra == 'x' or letra == 'X':
        continue
    elif letra == 'q' or letra == 'Q':
        break
    else:
        print(f'Você digitou {letra}')
print('Programa encerrado!')
