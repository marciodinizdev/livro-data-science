#1
var1 = 10
var2 = 20
var3 = 15
print('Analisando as variáveis...')
if(var1 > var2 and var1 < var3) or (var1 < var2 and var1 > var3):
    print(f'O valor mediano é {var1}')
elif(var2 > var1 and var2 < var3) or (var2 < var1 and var2 > var3):
    print(f'O valor mediano é {var2}')
else:
    print(f'O valor mediano é {var3}')

#2
lado1 = 4
lado2 = 3
lado3 = 7

if lado1**2 + lado2**2 == lado3**2:
    print(f'Temos que: {lado1}² + {lado2}² = {lado3}².')
    print(f'Assim teremos {lado1**2} + {lado2**2} = {lado3**2}')
    print("Portanto pelo Teorema de Pitágoras, temos um triângulo retângulo")
else:
    print(f'Temos que: {lado1}² + {lado2}² != {lado3}².')
    print(f'Assim teremos {lado1**2} + {lado2**2} != {lado3**2}')
    print("Portanto pelo Teorema de Pitágoras, NÃO temos um triângulo retângulo")

#3
import random
sorteios = [random.randint(0, 1) for _ in range(11)] # Realiza o sorteio 10 vezes
print('Números sorteados', sorteios)

c_azul = sorteios.count(0) # Conta o número de ocorrências de 0
c_vermelho = sorteios.count(1) # Conta o número de ocorrências de 1

print(f'A bolinha AZUL foi sorteada {c_azul} vezes!')
print(f'A bolinha VERMELHA foi sorteada {c_vermelho} vezes!')

if c_azul > c_vermelho:
    print('Bolinha AZUL apareceu mais vezes')
else: 
    print('Bolinha VERMELHA apareceu mais vezes')