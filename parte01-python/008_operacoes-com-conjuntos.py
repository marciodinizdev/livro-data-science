A = set() # Criando um conjunto vazio
print('Criando o conjunto vazio A =', A)

A.add('X') # Adicionando um elemento ao conjunto
print('X foi adicionado ao conjunto A! Agora A =', A)
A.add('Y')
print('Y foi adicionado ao conjunto A! Agora A =', A)
A.add('Z')
print('Z foi adicionado ao conjunto A! Agora A =', A)
A.add(123)
print('123 foi adicionado ao conjunto A! Agora A =', A)

# Contando os elementos de A
print(f'Conjunto A agora tem {len(A)} elementos')

# Testando a pertinencia em A
elemento_testado = 'A' # Criada uma variável a ser testada
teste_pertinencia = elemento_testado in A # Teste que retorna True ou False
print(f'O elemento \'{elemento_testado}\' está contido em A?')
if teste_pertinencia == True:
    print("Sim!")
else:
    print('Não!')

print('\n-Tópico 2-\n') # Tópico 2

# Usando conjuntos para eliminar elementos duplicados de uma lista 
lista_duplicados = ['A', 'B', 'C', 'B', 'A', 'C']
print('Conteúdo inicial da lista:', lista_duplicados)
print('Convertendo a lista em conjunto para eliminar duplicidades...')
conjunto = set(lista_duplicados) # Transforma lista em um conjunto atravéws da função set()
print('A lista agora virou o conjunto', conjunto)
print('Convertendo o conjunto em uma lista sem duplicidades...')
lista_sem_duplicados = list(conjunto) # list() transforma o conjunto em uma lista
print('Conteúdo da lista sem valores duplicados:', lista_sem_duplicados)

# OBS: como conjuntos são coleções que não permitem duplicidades, uma vez que transformamos a lista em um conjunto, seus elementos repetidos são automaticamente eliminados

# OBS 2: Após o conjunto fazer seu trabalho de excluir duplicações, retornamos nossa coleção ao formato de lista