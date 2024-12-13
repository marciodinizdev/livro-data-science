#1
eh_par = (57%2==0)
print(eh_par)
# O resultado é um boolean False pois % calcula o resto da divisão entre 2 números, e se o resultado for 0 o número é par, o que não é o caso aqui

#2
a = 2
b = -3
c = -2

delta = (b**2) - 4*a*c
print(delta)

#3
def delta():
    print((b**2) - 4*a*c)
delta()

#4
palavra = 'Teste'
numero = 15
boleano = True

print('Usando %: ', end='')
print('palavra = %s, numero = %d, boleano = %s' % (palavra, numero, boleano))

print(f'Usando f: palavra: {palavra}, numero: {numero}, boleano: {boleano}')