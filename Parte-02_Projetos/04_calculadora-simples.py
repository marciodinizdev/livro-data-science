'''
Programa que implementa uma função chamada calculadora que recebe dois números e uma operação (+, -, *, /) e retorna o resultado. 

O programa deve pedir os dados ao usuário e exibir o resultado.
'''
def calculadora(numero1, operacao, numero2):
    if operacao =='+' :
        resultado = numero1 + numero2
    elif operacao == '-':
        resultado =  numero1 - numero2
    elif operacao == '*':
        resultado =  numero1 * numero2
    elif operacao == '/':
        resultado = numero1 / numero2
    else:
        return 'Operação inválida'
    
    # Se o resultado for um número inteiro, retorna o número inteiro. Caso contrário, retorna o número real
    if resultado.is_integer():
        return int(resultado)
    
    return resultado

numero1 = float(input('Digite o primeiro número: '))
operacao = input('Digite a operação (+, -, *, /): ')
numero2 = float(input('Digite o segundo número: '))

print(f'O resultado da operação é: {calculadora(numero1, operacao, numero2)}')