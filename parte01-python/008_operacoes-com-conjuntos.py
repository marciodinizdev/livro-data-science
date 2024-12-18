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