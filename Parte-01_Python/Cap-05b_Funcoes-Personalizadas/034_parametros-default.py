### É possível definir valores padrão (default) para os parâmetros de uma função personalizada.
# Se um valor padrão for definido para um parâmetro, ele se torna opcional e pode ser omitido ao chamar a função.

def soma(a, b=5):
    return a + b
# Somando um número com o valor padrão 5
print(soma(3))
# Somando dois números ignorando o valor padrão
print(soma(3, 8))
