import math

def fun(x):
    return math.sin(x)


def converter_intervalo(alfa, a, b):
    return ((b + a) / 2) + ((b - a) / 2) * alfa

    
def gauss_legendre(a, b, n):
    pesos = []
    if n == 2:
        pesos[0] = pesos[1] = 1
        pontos = [-0.5773502692, 0.5773502692]
    elif n == 3:
        pesos[0] = pesos[2] = 0.5555555556
        pesos[1] = 0.8888888889
        pontos = [-0.7745966692, 0, 0.7745966692]
    elif n == 4:
        pesos[0] = pesos[3] = 0.3478548451
        pesos[1] = pesos[2] = 0.6521451549
        pontos = [-0.8611363116, -0.3399810436, 0.3399810436, 0.8611363116]

    valores_x = []
    for i in range(n):
        valores_x[i] = converter_intervalo(pontos[i], a, b)
        valor += pesos[i] * fun(valores_x[i])
    valor *= (b -a)/2
    return valor 