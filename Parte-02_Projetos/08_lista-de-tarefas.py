tarefas_pendentes = ['Estudar']
tarefas_concluidas = ['Trabalhar']
lista_de_tarefas = tarefas_pendentes + tarefas_concluidas  # Lista completa unificada para exibição

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
            tarefa_pendente = input('Digite a tarefa que deseja Adicionar: ').capitalize()
            if tarefa_pendente in tarefas_pendentes:
                while True:
                    print(f'{tarefa_pendente} já existe na lista de tarefas.\n')
                    tarefa_ou_sair = input('Adicione uma nova ou digite S para sair: ').capitalize()
                    if tarefa_ou_sair == 'S':
                        break
                    else:
                        tarefas_pendentes.append(tarefa_ou_sair)
                        print(f'{tarefa_ou_sair} foi adicionado à lista de tarefas!')
            else:
                tarefas_pendentes.append(tarefa_pendente)
                print(f'{tarefa_pendente} foi adicionado à lista de tarefas!')
        
        elif opcao == '2':
            if len(tarefas_pendentes) == 0:
                print('Você não tem tarefas pendentes!')
            else:
                print('Digite o número da tarefa para marcar como concluída:')
                for indice_tarefa_pendente, tarefa_pendente in enumerate(tarefas_pendentes, start=1):
                    print(f'{indice_tarefa_pendente}. {tarefa_pendente}')
                try:
                    tarefa_escolhida = int(input('\nMarcar como concluída (digite o número): '))
                    if 1 <= tarefa_escolhida <= len(tarefas_pendentes):
                        tarefa_escolhida = tarefas_pendentes.pop(tarefa_escolhida - 1)
                        tarefas_concluidas.append(tarefa_escolhida)
                        print(f'Tarefa "{tarefa_escolhida}" foi marcada como concluída!')
                    else:
                        print('Número inválido! Escolha um número da lista.')
                except ValueError:
                    print('Entrada inválida! Digite um número.')
        
        elif opcao == '3':
            if len(tarefas_pendentes) + len(tarefas_concluidas) == 0:
                print('Você não tem tarefas!')
            else:
                print('Digite o número da tarefa para excluir:')
                # Exibe todas as tarefas, pendentes e concluídas
                todas_tarefas = tarefas_pendentes + tarefas_concluidas
                for indice, tarefa in enumerate(todas_tarefas, start=1):
                    status = "[Pendente]" if tarefa in tarefas_pendentes else "[Concluída]"
                    print(f'{indice}. {tarefa} {status}')
                
                try:
                    tarefa_escolhida = int(input('\nExcluir (digite o número): '))
                    if 1 <= tarefa_escolhida <= len(todas_tarefas):
                        tarefa_removida = todas_tarefas.pop(tarefa_escolhida - 1)
                        # Remove a tarefa da lista correspondente
                        if tarefa_removida in tarefas_pendentes:
                            tarefas_pendentes.remove(tarefa_removida)
                        elif tarefa_removida in tarefas_concluidas:
                            tarefas_concluidas.remove(tarefa_removida)
                        print(f'Tarefa "{tarefa_removida}" foi removida da lista!')
                    else:
                        print('Número inválido! Escolha um número da lista.')
                except ValueError:
                    print('Entrada inválida! Digite um número.')
        
        elif opcao == '4':
            print('Finalizando a lista de tarefas...')
            break
        
        else:
            print('Opção inválida! Tente novamente.')

gerenciar_tarefas()
print(f'\nLista de tarefas completa!')
print(f'Tarefas Pendentes: {tarefas_pendentes}')
print(f'Tarefas Concluídas: {tarefas_concluidas}')
