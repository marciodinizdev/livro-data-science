# Dicionário é um tipo de dado que agrupo atributos por meio de chave e valor

clientes = {} # Criando um dicionário vazio
funcionarios = dict() # Outra forma de criar
pesos = {'Márcio': 80.2, 'Lays': 57.5} 
print('Dicionários:', clientes, funcionarios, pesos)

# Criando um dicionário para informações de um produto
produto = {
    'codigo': '00835-B',
    'nome': 'Chave de Rosca 27',
    'preco': 29.579
}
print(f'Cadastrando produto: {produto}')
print(f'Código do produto: {produto["codigo"]}')
print(f'Nome do produto: {produto["nome"]}')
print(f'Preço do produto: R$ {produto["preco"]:.2f}')
produto['preco'] = 19.901
print('Alterando preço do produto...')
print(f'Novo preço do produto: {produto["preco"]:.2f}')