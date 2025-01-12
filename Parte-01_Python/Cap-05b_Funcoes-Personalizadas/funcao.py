### Uma função é um bloco de código que executa uma tarefa específica e serve para organizar o código e reutilizar o código

# Definindo uma função personalizada que soma dois números
def soma(a, b):

    return a + b

# Definindo uma função personalizada que calcula o fatorial de um número
def fatorial(n):

    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
def delta(a, b, c):

    # O delta é o valor de b² - 4ac.
    resultado = b ** 2 - 4 * a * c
    return resultado

# Definindo uma função personalizada que verifica se um número é primo
def eh_primo(num):
    
    # Um número primo é um número maior que 1 que não tem divisores positivos além de 1 e ele mesmo.
    
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Usando as funções personalizadas
print(soma(3, 5)) # Soma 3 e 5
print(fatorial(5)) # Calcula o fatorial de 5
print(delta(1, 5, 6)) # Calcula o delta da equação de segundo grau com a = 1, b = 5 e c = 6
print(eh_primo(7)) # Verifica se 7 é um número primo
print(eh_primo(10)) # Verifica se 10 é um número primo