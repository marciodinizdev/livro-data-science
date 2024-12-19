# Funções que recebem uma quantidade de parâmetros e contém uma expressão em seu corpo

# Formato: lambda p1, p2, p3: expressao

# Expressão para calcular o delta de uma equação de 2º grau
delta = lambda a, b, c: b**2 - 4*a*c
print('Usando uma expressão lambda para calcular delta(1, 12, -13):')
print(f'delta = {delta(1, 12, -13)}')

# Expressão lambda para calcular média do aluno
media_aluno = lambda nota1, nota2, nota3: (nota1 + nota2 + nota3) / 3
print('Usando lambda para saber se o aluno foi aprovado ou reprovado...')
media = media_aluno(0, 8, 7)
if media >= 7.0:
    print(f'A média do aluno foi: {media:.1f}')
    print('Aluno aprovado!')
else:
    print(f'A média do aluno foi: {media:.1f}')
    print('Aluno reprovado!')