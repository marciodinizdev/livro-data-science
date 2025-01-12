#1 - Calculando o coeficiente angular de uma reta
def angular(x1, y1, x2, y2):
    delta_y = y2 - y1
    delta_x = x2 - x1
    m = delta_y / delta_x

    if m > 0:
        return f'O coeficiente angular é positivo: {m}'
    elif m < 0:
        return f'O coeficiente angular é negativo: {m}'
    else:
        return f'm -> infinito (coeficiente angular tende ao infinito)'
    
print(angular(1, 4, 3, 4))

#2 - Calculando a capacidade de um reservatório
def capacidade(altura, largura, comprimento):
    volume = altura * largura * comprimento
    capacidade = volume * 1000
    return f'A capacidade do reservatório é de {capacidade} litros'
print(capacidade(2, 1, 1.5))

#3 - Calculando o consumo total de combustível
def consumo_total(distancia_km, consumo_km_litro):
    consumo_total = distancia_km / consumo_km_litro
    return f'O consumo total de combistível é de {consumo_total} litros'
print(consumo_total(500, 12))