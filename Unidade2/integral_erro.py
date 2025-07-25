import math
import integral

def fun(x):
    return math.sin(x)


def integral_erro(a, b, e):
    erro = n = 1
    area_old = 0
    while erro > e:
        n = n*2
        area_new = integral.integral(a, b, n)
        erro = math.fabs((area_new - area_old)/area_new)
        area_old = area_new
    return area_new