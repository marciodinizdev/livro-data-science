### A função bool() é usada para converter qualquer valor em um True ou False.

# Valores que são considerados False
print(bool(False))
print(bool(0)) 
print(bool(0.0))
print(bool(''))
print(bool(None))
print(bool([]))
print(bool({}))
print(bool(set()))

# Valores que são considerados True
print(bool(True))
print(bool(1))
print(bool(3.14))
print(bool('texto'))
print(bool([1, 2, 3]))
print(bool({'chave': 'valor'}))
print(bool({1, 2, 3}))