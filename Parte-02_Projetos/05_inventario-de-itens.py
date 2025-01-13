'''
Sistema que simula um inventário de itens de uma loja de informática. O programa deverá:

1 -> Permitir adicionar itens ao inventário.
2 -> Permitir remover itens.
3 -> Exibir o inventário completo.

'''
inventario = []
print('Bem vindo ao inventário!\n')
while True:
    print('Digite a opção desejada:')
    print('1 -> Adicionar item.')
    print('2 -> Remover item.')
    print('3 -> Exibir inventário.')
    print('4 -> Sair.\n')

    opcao = input('Opção: ')
    if opcao == '1':
        item = input('Digite o nome do item que deseja adicionar: ').capitalize()
        if item in inventario:
            print(f'{item} já está no inventário.\n')
        else: 
            inventario.append(item)
            print(f'{item} foi adicionado ao inventário!\n')
    elif opcao == '2':
        if len(inventario) == 0:
            print('O inventário está vazio.\n')
        else:
            item = input('Digite o nome do item que deseja remover: ').capitalize()
            if item in inventario:
                inventario.remove(item)
                print(f'{item} foi removido ao inventário!\n')
            else:
                print(f'{item} não está no inventário.\n')  
    elif opcao == '3':
        if len(inventario) > 0:
            print(f'Itens atualmente no inventário: {inventario}\n')
        else:
            print('O inventário está vazio.\n')
    elif opcao == '4':
        print(f'O inventário completo é: {inventario}\n')
        print('Obrigado por usar o inventário. Até a próxima!')
        break
    else:
        print('Opção inválida. Tente novamente.\n')