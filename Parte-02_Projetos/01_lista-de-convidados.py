'''
Programa que recebe nomes de convidados para uma festa e os armazena em uma lista. Ao final, exibe:

1 -> Quantos convidados foram adicionados.
2 -> A lista completa de convidados.
3 -> Uma mensagem personalizada para cada convidado, como: "Bem-vindo, [nome]! Estamos ansiosos para a festa!".

'''
convidados = []
while True:
    nome = input('Digite o nome do convidado ou "sair" para encerrar: ').capitalize()
    if nome.lower() == 'sair':
        break
    convidados.append(nome)
    print(f'{nome} foi adicionado à lista de convidados.\n')

print(f'Foram adicionados {len(convidados)} convidados à lista. \n')
print(f'Lista de convidados: {convidados}\n')

print('Mensagens para os convidados:\n')
for convidado in convidados:
    print(f'Bem-vindo, {convidado}! Estamos ansiosos para a festa!\n')