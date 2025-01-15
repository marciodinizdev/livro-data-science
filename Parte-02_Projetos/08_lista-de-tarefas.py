'''
Programa para criar uma lista de tarefas com as condições:

1 -> O usuário deve ser capaz de adicionar uma tarefa, marcar como concluída ou removê-la.
2 -> O programa deve exibir a lista completa com as tarefas organizadas em "Concluídas" e "Pendentes".

'''
lista_de_tarefas = ['Estudar']

def gerenciar_tarefas():

    while True:
        print('')
        print('Digite a opção desejada:')
        print('Opção 1 -> Adicionar tarefa')
        print('Opção 2 -> Marcar tarefa como Concluída')
        print('Opção 3 -> Remover tarefa')
        print('Opção 4 -> Finalizar lista\n')
        opcao = input('Opção: ')
        print('')

        if opcao == '1':
            tarefa = input('Digite a tarefa que deseja Adicionar: ').capitalize()
            if tarefa in lista_de_tarefas:
                while True:
                    print(f'{tarefa} já existe na lista de tarefas.\n')
                    tarefa_ou_sair = input('Adicione uma nova ou digite S para sair: ').capitalize()
                    if tarefa_ou_sair == 'S':
                        break
                    else:
                        lista_de_tarefas.append(tarefa_ou_sair)
                        print(f'{tarefa_ou_sair} foi adicionado à lista de tarefas!')
            else:
                print(f'{tarefa} foi adicionado à lista de tarefas!')

    
    
print(f'Lista de tarefas: {lista_de_tarefas}')
gerenciar_tarefas()