# # Extendendo Listas
# usuarios = []
# usuarios_informatica = ["Anderson", "Bruno", "Carlos"]
# usuarios_contabilidade = ["Denise", "Edna", "Franciele"]

# print("Lista vazia: ", usuarios)
# print("Usuários de informática: ", usuarios_informatica)
# print("Usuários de contabilidade: ", usuarios_contabilidade)

# print("- Unindo as listas - \nPrimeiro, testando com Informática:")
# usuarios.extend(usuarios_informatica)
# print(usuarios)

# print("Agora adicionando Contabilidade:")
# usuarios.extend(usuarios_contabilidade)
# print(usuarios)

# # Inserindo elementos no meio de uma lista
# ferramentas = ["Alicate", "Prego", "Parafuso"]
# print("Lista inicial de ferramentas: ", ferramentas)
# ferramentas.insert(2, "Martelo")
# print("Lista nova de ferramentas: ", ferramentas)
# ferramentas.insert(0, "Chave estrela")
# print("Lista final de ferramentas: ", ferramentas)

# # Ordenando elementos da lista
# ferramentas.sort()
# print("Lista ordenada de ferramentas: ", ferramentas)

# Fatiando listas
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Lista original: ", numeros)

primeiro_numero = numeros[0]
print("Primeiro número: ", primeiro_numero)

ultimo_numero = numeros[-1]
print(f'Último número: {ultimo_numero}')

penultimo_numero = numeros[-2]
print(f'Penúltimo número: {penultimo_numero}')

quatro_primeiros_numeros = numeros[:4]
print(f'Quatro primeiros números: {quatro_primeiros_numeros}')

tres_ultimos_numeros = numeros[-3:]
print(f'Três últimos números: {tres_ultimos_numeros}')

sem_os_extremos = numeros[1:-1]
print(f'Sem o primeiro e o último número: {sem_os_extremos}')

sem_os_extremos_pulando2 = numeros[1:-1:2]
print(f'Sem o primeiro e o último número pulando de 2 em 2 números: {sem_os_extremos_pulando2}')

numeros_copia = numeros[:]
print(f'Realizando uma cópia da lista inteira: {numeros_copia}')

numeros_copia_pulando2 = numeros[1:-1:2]
print(f'Realizando uma cópia da lista inteira pulando de 2 em 2 números: {numeros_copia_pulando2}')

# OBS: a notação padrão de slicing usa intervalos abertos e fechados da matemática [1:-1], sendo abertos à direita e fechados à esquerda, ou seja, o primeiro elemento é sempre incluído (intervalo fechado à esquerda) e o último é excluído (intervalo aberto à direita). A lista completa permanece se nenhum elemento delimitador for adicionado [:]

# OBS2: O padrão de slice usa o formato: lista[inicio : fim : salto], quando o salto não é especificado, como na variável sem_os_extremos = numeros[1:-1], ele é considerado 1, já na variável sem_os_extremos_pulando2 = numeros[1:-1:2], o valor do salto é especificado como 2
