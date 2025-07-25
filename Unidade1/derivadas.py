import math

def fun(x):
    return math.sin(x)

def derivada_recursiva(x, deltax, direcao, ordem):
    if ordem == 0:
        return fun(x)
    else:
        if direcao == 1: #forward
            return (derivada_recursiva(x+deltax, deltax, direcao, ordem-1)-derivada_recursiva(x, deltax, direcao, ordem-1))/deltax
        elif direcao == 2: #backward
            return (derivada_recursiva(x, deltax, direcao, ordem-1) - derivada_recursiva(x - deltax, deltax, direcao, ordem-1)) / deltax
        elif direcao == 3: #central
            return (derivada_recursiva(x + deltax, deltax, direcao, ordem-1) - derivada_recursiva(x - deltax, deltax, direcao, ordem-1)) / (2*deltax)
        else:
            print("Direção inválida para derivada")

x = int(input("Entre com o valor de x: "))
deltax = int(input("Entre com o valor de DeltaX: "))
direcao = int(input("Escolha a Filosofia: 1 (Forward), 2 (Backward), 3 (Central) "))
ordem = int(input("Entre com a ordem da Derivada: 1 (Primeira), 2(Segunda), 3(Terceira)... "))

resultado = derivada_recursiva(x, deltax, direcao, ordem)
print(f'O resultado para as entradas de X = {x}, DeltaX = {deltax}, Filosofia = {direcao} (1 (Forward), 2 (Backward), 3 (Central)) e Ordem da Derivada = {ordem} é:\n {resultado}')