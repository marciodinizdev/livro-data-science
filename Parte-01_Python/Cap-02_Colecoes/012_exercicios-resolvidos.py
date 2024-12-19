# 1
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Sétimo elemento: {valores[6]}')
print(f'Lista completa {valores}')

valores_extenso = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']
lista_composta = [valores, valores_extenso]
print(f'Lista por extenso: {valores_extenso}')
print(f'Lista composta: {valores, valores_extenso}')
print(f'Primeiro elemento de cada lista: "{lista_composta[0][0]}" e "{lista_composta[1][0]}"')
print(f'Último elemento de cada lista: "{lista_composta[0][-1]}" e "{lista_composta[1][-1]}"')

#2 a)
itens = []
itens.append('livro')
itens.append('caderno')
itens.append('borracha')
print('Lista de ítens:', itens)

#2 b)
itens[1] = 'régua'
print('Lista de ítens:', itens)

#2 c)
pertinencia_caderno = 'caderno' in itens
if pertinencia_caderno == True:
    print('A lista contém um caderno')
else:
    print('A lista NÃO contém um caderno')

#2 d)
print('Quantidade de elementos na lista:', len(itens))
itens.pop(-1)
print('Lista de ítens:', itens)
print('Quantidade de elementos na lista:', len(itens))

#2 e)
fatia = itens[-2:]
print(f'Últimos dois ítens da lista: {fatia}')

#3
itens.insert(0, 'caderno')
print(f'Inserindo "caderno" na posição 0 da lista...')
print(f'Lista atualizada: {itens}')

#4
conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {0, 2, 4, 6, 8, 10}

uniao_AB = conjunto_A.union(conjunto_B)
print('A união com B =', uniao_AB)

interseccao_AB = conjunto_A.intersection(conjunto_B)
print('A intersecção com B = ', interseccao_AB)
