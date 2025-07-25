import math

def fun(x):
    return math.sin(x)

def newtoncottes_aberto_meio_2_3_4_pontos(a, b):
    m = (a + b) / 2
    r = (b - a) * fun(m)
    return r

def newtoncottes_aberto_grau1_2pontos(a, b):
    h = (b - a) / 3
    r = (3/2) * h * (fun(a+h) + fun(a+2*h))
    return r

def newtoncottes_aberto_grau2_3pontos(a, b):
    h = (b - a) / 4
    r = (4/3) * h * (2*fun(a+h) - fun(a+2*h) + 2*fun(a+3*h))
    return r

def newtoncottes_aberto_grau3_4pontos(a, b):
    h = (b - a) / 5
    r = (5/24) * h * (11*fun(a+h) + fun(a+2*h) + fun(a+3*h) + 11*fun(a+4*h))
    return r

def newtoncottes_aberto_grau4_5pontos(a, b):
    h = (b - a) / 6
    r = (6/20) * h * (11 * fun(a + h)- 14 * fun(a + 2 * h)+ 26 * fun(a + 3 * h)- 14 * fun(a + 4 * h)+ 11 * fun(a + 5 * h))
    return r 
