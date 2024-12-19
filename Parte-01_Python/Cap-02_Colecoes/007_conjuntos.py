# Usa a notação de chaves {}
# Pode ser criado adicionando explicitamente os elementos
conjunto_pares = {0, 2, 4, 6, 8}

# Ou usando a função set()
conjunto_impares = set({1, 3, 5, 7, 9})

print('Conjunto pares:', conjunto_pares)
print('Conjunto ímpares', conjunto_impares)

# OBS: Sempre que precisar criar um conjunto vazio use a função set() pois ao criar um conjunto vazia explicitamente você criará uma outra coleção chamada dicionáario
# Portanto
conjunto_vazio = set()
print('Conjunto vazio:', conjunto_vazio)

# Adicionando elementos ao conjunto vazio
conjunto_vazio.add('Não é mais vazio')
print('Conjunto vazio:', conjunto_vazio)