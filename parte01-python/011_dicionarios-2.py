# Examinando várias chaves/valores em um dicionário
jogo = {
    "codigo": "00047-A",
    "Nome": "Elden Ring",
    "preco": 349.00
}
print(f'Chaves do jogo: {jogo.keys()}')
print(f'Valores do jogo: {jogo.values()}')
print(f'Tuplas(chave, valor) do jogo: {jogo.items()}')

# Removendo elementos de um dicionário
del jogo["preco"]
print('Removendo o preço do jogo...')
print(f'Tuplas(chave, valor) do jogo: {jogo.items()}')

# Usando defaultdict para retornar um valor ao invés de um KeyError ao buscar uma chave inexistente

# O defaultdict é uma classe que precisa ser importada
from collections import defaultdict

genero = defaultdict(lambda: 'Shooter')
genero['Balatro'] = 'Cardgame'
genero['Final Fantasy'] = 'RPG'
print('Alguns gêneros cadastrados:')
print(f'Balatro: {genero["Balatro"]}')
print(f'Final Fantasy: {genero["Final Fantasy"]}')
print(f'Battlefield: {genero["Battlefield"]}')

# Usando a classe Counter para contar frequências em coleções

# Também precisa ser importada
from collections import Counter
lista_numeros = [1, 2, 2, 1, 2, 0]
lista_strings = ['A', 'B', 'B', 'A', 'C', 'A', 'A', 'C']
c1 = Counter(lista_numeros)
c2 = Counter(lista_strings)

print(f'Lista de números: {lista_numeros}')
print(f'Distribuição de números: {c1}')
print(f'Lista de strings: {lista_strings}')
print(f'Distribuição de strings: {c2}')