# While executa um determinado suóte de código enquanto (while) uma certa condição for satisfeita

# Exemplo
quantidade = 0 # define uma quantidade inicial
while quantidade < 10:
    print('Quantidade:', quantidade) # mostra a quantidade atual
    quantidade = quantidade + 1 # adiciona + 1
# Encerra a execução quando a quantidade atinge o valor no while
print("Quantidade máxima atingida. Programa encerrado!")

# Calculando o produto de uma sequência de números
n = 5 # representa o número até onde o produto será calculado
contador = 0 # começa a contagem do loop.
resultado = 1 # inicializa o valor do produtório com 1
while contador < n:
    contador = contador + 1
    resultado = resultado * contador
    print(contador, end=" ") # imprime o valor atual do contador a cada execução e o end=" " previne a quebra de linha entre os valores

print(f'\nContador = {contador}')
print(f'produtório = {resultado}')

