### Do while é um while mas que executa primeiro e testa uma condição depois, porém essa instrução não existem em Python
# Esse comportamento pode ser simulado com um loop while

continua = 'S'
somatorio = 0.0
quantidade = 0
while continua == 'S' or continua == 's':
    preco = float(input('Entre com o preço do próximo produto: '))
    somatorio = somatorio + preco
    continua = input('Acrescentar mais produtos? (S/N) ')
print('O valor total dos produtos é R$ %.2f' %somatorio)