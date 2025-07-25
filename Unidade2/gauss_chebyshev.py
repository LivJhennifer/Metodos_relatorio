import math 

def fun(x):
    return math.sin(x)

def gauss_chebyshev(n):
    valor = 0
    peso = math.pi/n

    for i in range(n):
        ponto = math.cos((2*i-1)*math.pi/(2*n))
        valor += peso *fun(ponto)
    return valor