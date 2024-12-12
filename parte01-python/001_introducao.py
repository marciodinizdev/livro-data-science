print("Executando script...")

# Definimos teste1 globalmente
teste1 = 123
def funcao_f():
    
    # Definimos teste2 no escopo da função funcao_f
    # Mas usamos o modificador 'global' para expandir teste2 globalmente
    global teste2
    teste2 = 456
    
    # Usamos o método for para criar um loop de range 1 a 11
    # Definimos z dentro de funcao_f
    for x in range(1, 11):
        z = x * 2
        print(f'z = {z}')
    
    #Imprimimos z, teste 1 e teste2 dentro da função
    print(f'Valor de z após loop: {z}')
    print(f'Valor de teste1, dentro da função: {teste1}')
    print(f'Valor de teste2, dentro da função: {teste2}')

# Chamamos a função
funcao_f()

# Imprimimos teste1, teste2 e z fora da função
print(f'Valor de teste1 fora da função: {teste1}')
print(f'Valor de teste2 fora da função: {teste2}')
print((f'Valor de z após loop: {z}')) # Vai dar erro pois z só existe dentro da função