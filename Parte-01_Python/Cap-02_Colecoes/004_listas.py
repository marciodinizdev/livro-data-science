# Listas
carros_populares = ["Corsa", "HB20", "Ka"]
print("Carros populares: ", carros_populares)

carros_tunados = ["Ferrari", "Porshe", "Supra"]
print("Carros tunados: ", carros_tunados)

# Adicionando elementos na lista
carros_populares.append("Uno")
print(carros_populares[3], "foi adicionado!")
print("Lista de carros populares atualizada: ", carros_populares)

carros_tunados.append("Viper")
print(carros_tunados[3], "foi adicionado")
print("Lista de carros tunados atualizada: ", carros_tunados)

# Removendo elementos da lista pelo índice
print(carros_populares[1], "foi removido dos carros populares!")
carros_populares.pop(1)
print("Lista de carros populares atualizada: ", carros_populares)

# Removendo elementos da lista pelo nome do objeto
print("Porshe foi removido dos carros tunados!")
carros_tunados.remove('Porshe')
print("Lista de carros tunados atualizada: ", carros_tunados)

#Listas de listas
carros = [carros_populares, carros_tunados]
print(f'Lista de carros completa: {carros}')
print(f'Carro popular: {carros[0][0]}')
print(f'Carro popular: {carros_populares[0]}')
print(carros[0][0] == carros_populares[0])

# Obtendo o tamanho da lista
print('O número de carros na lista é:', len(carros_populares))

# Relações de pertinência
carro_tunado = 'Supra'
if carro_tunado in carros_tunados:
    print('Carro encontrado:', carro_tunado)

elif carro_tunado not in carros_tunados:
    print('Carro não cadastrado!')
