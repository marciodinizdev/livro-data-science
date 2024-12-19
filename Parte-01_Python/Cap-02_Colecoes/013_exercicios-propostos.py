#1
teste = [1, 2, 3, 4, 5]
print(f'Segundo elemento da lista: {teste[1]}')
print(f'Lista teste completa: {teste}')

#2
teste2 = [6, 7, 8, 9, 10]
print(f'Lista test2 completa: {teste2}')
teste.extend(teste2)
print(f'Lista teste completa: {teste}')

#3
primos = {2, 3, 5, 7, 11, 13, 17, 19}
pares = {0, 2, 4, 6, 8, 10}
impares = {11, 13, 15, 17, 19}

inter_primos_impares = primos.intersection(impares)
uniao_pares = pares.union(inter_primos_impares)
print('Pares união (primos intersecção ímpares)', uniao_pares)

#4
dna = 'CGCGGACCTTTCCCAAA'
dna_em_lista = list(dna) # Transforma uma string em lista
print(dna_em_lista)

from collections import Counter
contagem_caracteres = Counter(dna_em_lista)
print('Distribuição de letras:', contagem_caracteres)