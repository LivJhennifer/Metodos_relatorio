import math
def fun(x):
    return math.sin(x)

def integral(a, b, n):
    Dx = (b-a)/n
    area = 0
    for i in range(n):
        xi = a + Dx/2 + i*Dx
        area = area + Dx*fun(xi)
    return area