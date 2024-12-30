### A instrução for tem muitos formatos e muitas utilidades

# Para iterar sobre uma coleção criamos uma variável para apresentar cada elemento da lista
jogos = ["Final Fantasy", "Elden Ring", "Forza Horizon", "Astrobot"]

for jogo_atual in jogos: 
    print('O jogo atualmente examinado é: %s' %jogo_atual) # exibe elemento por elemento até acabar a lista

# Para iterar um número predeterminado de vezes usamos um loop for com a funçlão range(tamanho)
for x in range(20):
    print("Aprendendo Python de um jeito simples!") # vai exibir a mensagem 20 vezes graças ao range(20)

### É possível usar o conteúdo da variável de controle dentro do suíte e aproveitar das várias formas da função range()
print('Imprimindo os números de 0 a 9...')
for x in range(10): # gera uma sequência de 10 números começando com 0
    print(x, end=" ")

print('\nImprimindo os números de 1 a 10...')
for x in range(1, 11): 
    print(x, end=" ")

print('\nImprimindo os números ímpares de 1 a 10...')
for x in range(1, 11, 2):
    print(x, end=" ")

print('\nImprimindo os números pares de 0 a 10...')
for x in range(0, 10, 2):
    print(x, end=" ")

print('\nContagem regressiva de 10 até 0...')
for x in range(10, -1, -1):
    print(x, end=" ")

### For pode ser usado para obter informações de coleções relacionadas por meio da função enumerate()
# for indice, variavel in enumerate(colecao)

alunos = ['Beatriz', 'Bruce', 'Maria Clara', 'João Pedro']
notas = [9.5, 8.0, 9.5, 8.0]
for indice, aluno in enumerate(alunos):
    print(f'Nome: {aluno} - Nota: {notas[indice]}')

### O loop for permite iterar sobre os caracteres de uma strings e imprimir letra por letra da frase

frase = "Aprendendo Python"
for c in frase:
    print(c)