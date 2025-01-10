### Função int()

# Convertendo string em int
a = '123'
a_int = int(a)
print(f'Convertendo a para inteiro: {a_int}')
print(f'Tipo de a: {type(a)}. Tipo de a_int: {type(a_int)}')

# Extraindo a parte inteira de um número
e = 2.718281
parte_inteira_de_e = int(e)
print(f'A constante e vale, aproximadamente: {e}')
print(f'A parte inteira de e vale: {parte_inteira_de_e}')

# Converetendo boolean para int
print(f'O boolean True equivale ao valor inteiro: {int(True)}')
print(f'O boolean False equivale ao valor inteiro: {int(False)}')