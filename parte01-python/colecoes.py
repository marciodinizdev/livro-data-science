carros_populares = ["Corsa", "HB20", "Ka"]
print("Carros populares: ", carros_populares)

carros_tunados = ["Ferrari", "Porshe", "Supra"]
print("Carros tunados: ", carros_tunados)

# carros_populares.append("Uno")
# print(carros_populares[3], " foi adicionado!")
# print("Lista de carros populares atualizada: ", carros_populares)

# carros_tunados.append("Viper")
# print(carros_tunados[3], " foi adicionado")
# print("Lista de carros tunados atualizada: ", carros_tunados)

# print(carros_populares[1], " foi removido!")
# carros_populares.pop(1)
# print("Lista de carros populares atualizada: ", carros_populares)

# print(carros_tunados[1], " foi removido")
# carros_tunados.pop(1)
# print("Lista de carros tunados atualizada: ", carros_tunados)

carros = [carros_populares, carros_tunados]
print(f'Lista de carros completa: {carros}')
print(f'Carro popular: {carros[0][0]}')
print(f'Carro popular: {carros_populares[0]}')
print(carros[0][0] == carros_populares[0])