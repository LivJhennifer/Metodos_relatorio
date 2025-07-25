import math
import newtoncotes_aberto
import newtoncottes_fechado

def integral_composta(a, b, n, metodo):
    h = (b - a) / n
    soma = 0
    for i in range(n):
        x0 = a + i * h
        x1 = x0 + h
        soma += metodo(x0, x1)
    return soma