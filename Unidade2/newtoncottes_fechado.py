import math

def fun(x):
    return math.sin(x)

def newtoncottes_fechado_grau1(a, b):
    r = (b - a) * (fun(a) + fun(b)) / 2
    return r

def newtoncottes_fechado_grau2(a, b):
    m = (a + b) / 2
    r = (b - a) * (fun(a) + 4*fun(m) + fun(b)) / 6
    return r

def newwtoncottes_fechado_grau3(a, b):
    h = (b - a)/3
    r = (3*h/8) * (fun(a) + 3*fun(a+h) + 3*fun(a+2*h) + fun(b))
    return r

def newtoncottes_fechado_grau4(a, b):
    h = (b - a) / 4
    r = ((2 * h) / 45) * (7 * fun(a)+ 32 * fun(a + h)+ 12 * fun(a + 2 * h)+ 32 * fun(a + 3 * h)+ 7 * fun(a + 4 * h))
    return r
