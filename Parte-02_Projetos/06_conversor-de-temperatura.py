'''
Programa que converte temperaturas entre Celsius, Fahrenheit e Kelvin. O programa deve:

1 -> Pedir ao usuário a temperatura e a unidade original.
2 -> Converter para as outras duas unidades.
3 -> Exibir os resultados.

'''
def converter_temperatura():

    temp = float(input('Digite o valor da temperatura: '))
    unidade_origem = input('Digite a unidade de origem (C, F, K): ').upper()

    # Fórmulas de conversão
    c_k = temp + 273.15
    c_f = (temp * 9/5) + 32
    f_c = (temp - 32) * 5/9
    f_k = (temp - 32) * 5/9 + 273.15
    k_c = temp - 273.15
    k_f = (temp - 273.15) * 9/5 + 32

    if unidade_origem == 'C':
        print(f'{temp}°C equivalem a {c_k:.2f}°K e a {c_f:.2f}°F')
    elif unidade_origem == 'F':
        print(f'{temp}°F equivalem a {f_c:.2f}°C e a {f_k:.2f}°K')
    elif unidade_origem == 'K':
        print(f'{temp}°K equivalem a {k_c:.2f}°C e a {k_f:.2f}°F')
    else:
        print('Digite uma unidade válida! (C, F, K)')

converter_temperatura()