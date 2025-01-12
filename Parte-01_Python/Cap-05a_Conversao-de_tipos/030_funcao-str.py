### A função str() é muito útil para converter valores em string para que possam ser concatenados com outras strings.

# Convertendo um número inteiro em string
numero_inteiro = 123
numero_como_string = str(numero_inteiro)
print(numero_como_string) 

# Convertendo um número float em string
numero_flutuante = 123.45
numero_como_string = str(numero_flutuante)
print(numero_como_string)

# Convertendo um valor booleano em string
valor_booleano = True
valor_como_string = str(valor_booleano)
print(valor_como_string)

# Convertendo uma lista em string
lista = [1, 2, 3]
lista_como_string = str(lista)
print(lista_como_string)

# Convertendo um dicionário em string
dicionario = {'chave': 'valor'}
dicionario_como_string = str(dicionario)
print(dicionario_como_string)

# Convertendo uma número em string dentro de uma string
codigo = 300
nome = 'Fulano'
mensagem = 'O código do cliente é ' + str(codigo) + ', e o nome dele é ' + nome
print(mensagem)  # Saída: 'O código do cliente é 300, e o nome dele é Fulano'

## Obs: Sem a conversão para string, o código acima resultaria em erro. Veja o exemplo abaixo:
mensagem = 'O código do cliente é ' + codigo + ', e o nome dele é ' + nome
print(mensagem)  # Saída: TypeError: can only concatenate str (not "int") to str