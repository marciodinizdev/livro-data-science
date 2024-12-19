# Os condicionais elif e else permitem executar outros códigos caso a condição do if não seja atendida
# O if testa uma condição
# Se o if não for atendido, o elif testa uma segunda condição
# Se nenhuma condição for atendida o else é executado

# Dada a variável
media = 2.5

print('Testando media...')
if media >= 7.0:
    print('Parabéns! Você foi aprovado!') 
elif media < 7.0 and media > 3.0:
    print('Você fará prova final.')
# Se nem o if nem o elif foraem atendidos:
else:
    print('Você foi reprovado! Estude mais!')

# ifs podem ser encadeados tendo um if de outro if
idade = 20
sexo = 'F'

if sexo == 'M':
    if idade >= 40:
        print('Você precisa fazer exame de próstata!')
    else:
        print('Você precisará fazer exame de próstata aos 40 anos.')
else:
    print('Mulheres não precisam fazer exame de próstata')

# Para resumir um condicional simples podemos usar Operadores Ternários
# A sintaxe é: expressao1 if condicao else expressao2
idade= 20
print(f'Pode votar' if idade >= 16 else 'Não pode votar')