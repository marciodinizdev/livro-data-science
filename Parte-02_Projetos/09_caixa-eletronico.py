'''
Programa que simula um caixa eletrônico. O sistema permite que o usuário realize as seguintes operações:

1 -> Ver Saldo
2 -> Depositar
3 -> Sacar
4 -> Sair

'''
# Funcão depositar
def depositar(saldo):

    while True:
        valor_depositado = input('Digite o valor que deseja depositar ou tecle S pra sair: ').strip().lower()
        if valor_depositado == 's':
            break
        elif valor_depositado.isnumeric():
            valor_depositado = int(valor_depositado)
            if valor_depositado == 0:
                print('Você não pode depositar 0. Escolha um valor positivo: ')
            else:
                saldo = saldo + valor_depositado
                print(f'R$ {valor_depositado} depositado com sucesso! Saldo atual: R$ {saldo}')

        else:
            print('Valor inválido! Digite um número ou S para sair.')
    return saldo
    
# Função sacar
def sacar(saldo):

    while True:
        valor_sacado = input('Digite o valor que deseja sacar ou tecle S para sair: ')
        if valor_sacado == 's':
            break
        elif valor_sacado.isnumeric():
            valor_sacado = int(valor_sacado)
            if valor_sacado > saldo:
                print(f'Saldo insuficiente! Escolha um valor até R$ {saldo}: ')
            else:
                saldo = saldo - valor_sacado
                print(f'R$ {valor_sacado} sacado com sucesso! Saldo atual: R$ {saldo}')
        else:
            print('Valor inválido! Digite um número ou S para sair.')
    
    return saldo

# Função caixa eletrônico
def caixa_eletronico():

    saldo = 0

    while True:
        print('\n ====== Caixa Eletrônico ======')
        print('')
        print('1. Ver Saldo')
        print('2. Depositar')
        print('3. Sacar')
        print('4. Encerrar Operação')
        inicio_opcao = input('\nOpção (digite o número): ')

        if inicio_opcao == '1':
            print(f'Saldo atual: R$ {saldo:.2f}')
        
        elif inicio_opcao == '2':
            saldo = depositar(saldo)
        
        elif inicio_opcao == '3':
            saldo = sacar(saldo)
        
        elif inicio_opcao == '4':
            print('Obrigado por usar o Caixa Eletrônico!')
            break
        
        else:
            print('Opção inválida! Tente novamente.')

caixa_eletronico()