# CUIDADO! Loops infinitos serão executados eternamente até o programa travar ou você encerrar com ctrl+C em caso de execução no terminal

# Exemplo
while True:
    print("Loop infinito em execução...")

# O exemplo a seguir irá executar infinitamente pois nada nele fará o x deixar de ser maior que 0
x = 1
while x > 0:
    print("Loop infinito em execução...")