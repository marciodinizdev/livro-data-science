#1 Calculando a distância entre dois pontos
from math import sqrt
def calcular_distancia(x1, y1, x2, y2):
    distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return f'A distância entre os pontos é: {distancia:.2f}'
print(calcular_distancia(2, 3, 6, 7))

#2 - Calculando o preço total de um tanque de água
def calcular_preco(altura, largura, comprimento, preco_litro):
    volume = altura * largura * comprimento
    quantidade_litros = volume * 1000
    custo = quantidade_litros * preco_litro
    return f'A capacidade do reservatório é de {quantidade_litros} litros e o custo total é de R$ {custo:.2f}'
print(calcular_preco(2, 1, 1.5, 3.59))

#3
def calcular_custo_combustivel(distancia_km, consumo_km_litro, preco_litro):
    consumo_total = distancia_km / consumo_km_litro
    custo_total = consumo_total * preco_litro
    return f'O custo total para percorrer {distancia_km} km é de R$ {custo_total:.2f}'
print(calcular_custo_combustivel(600, 10, 5))