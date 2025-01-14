'''
Programa que recebe uma lista de nomes e realiza um sorteio para escolher um deles. Depois exibe o nome sorteado.

'''
import random

def sorteio(lista_nomes):
    if not lista_nomes:
        print('A lista está vazia!')
    
    else:
        nome = random.choice(lista_nomes)
    return f'O vencedor é: {nome}!'

lista_nomes = ["Ramon", "Renato", "Rafael", "Ricardo", "Paulo", "Márcio", "Maurício", "Mário", "Marcelo", "Miguel", "Matheus", "Márcia", "Mariana", "Marta", "Mônica", "Michele", "Mirela", "Mila", "Mara", "Margarida"]

print(sorteio(lista_nomes))