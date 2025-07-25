import math

def fun(x):
    return math.sin(x)

def gauss_hermite(n):
    pesos = []
    pontos = []
    if n == 2:
        pesos[0] = pesos[1] = 0.8862269255
        pontos = [-0.7071067812, 0.7071067812]
    elif n == 3:
        pesos = [0.2954089756, 1.1816359006, 0.2954089752]
        pontos = [-1.2247448714, 0, 1.2247448714]
    elif n == 4:
        pesos = [0.0813128354, 0.8049140900, 0.8049140900, 0.0813128354]
        pontos = [-1.6506801239, -0.5246476233, 0.52464762328, 1.65068012389]
    for i in range(n):
        valor += pesos[i] * fun(pontos[i])


    return valor 