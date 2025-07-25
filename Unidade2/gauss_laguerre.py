import math

def fun(x):
    return math.sin(x)

def gauss_laguerre(n):
    if n == 2:
        pesos = [0.8535533906, 0.1464466094]
        pontos = [0.5857864376, 3.4142135624]
    elif n == 3:
        pesos = [0.7110930099, 0.2785177336, 0.0103892565]
        pontos = [0.4157745568, 2.2942803603, 6.2899450829]
    elif n == 4:
        pesos = [0.6031541043, 0.3574186924, 0.0388879085, 0.0005392947]
        pontos = [0.3225476896, 1.7457611012, 4.5366202969, 9.3950709123]
    for i in range(n):
        valor += pesos[i] * fun(pontos[i])
    return valor
