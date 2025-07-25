import numpy as np
import math

MAX_INTER = 100000000

def matriz_matriz(A, B):
    n = len(A)
    C = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def produto_escalar(v1, v2):
    return np.dot(v1, v2)

def matriz_vetor(matriz, vetor):
    n = len(matriz)
    res = [0.0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i] += matriz[i][j] * vetor[j]
    return res

def normalize(vetor, n):
    norma = math.sqrt(produto_escalar(vetor, vetor))
    for i in range(n):
        vetor[i] /= norma
    return vetor

def calcular_inversa(A):
    n = len(A)
    A_inv = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    temp = [row[:] for row in A]
    
    for i in range(n):
        if temp[i][i] == 0:
            raise ValueError("Matriz é singular e não pode ser invertida")
        
        diag = temp[i][i]
        for j in range(n):
            temp[i][j] /= diag
            A_inv[i][j] /= diag
        
        for k in range(n):
            if k != i:
                fator = temp[k][i]
                for j in range(n):
                    temp[k][j] -= fator * temp[i][j]
                    A_inv[k][j] -= fator * A_inv[i][j]
    
    return A_inv

def metodo_potencia_regular(A, v, e):
    y1_new = 0
    vk_new = v
    error = e + 1
    inter = 0 

    while error > e and inter < MAX_INTER:
        y1_old = y1_new
        x1_old = normalize(vk_new, len(vk_new))  
        vk_new = matriz_vetor(A, x1_old)
        y1_new = produto_escalar(x1_old, vk_new)
        if y1_new != 0:
            error = math.fabs((y1_new - y1_old)/y1_new)
        inter += 1

    return y1_new, x1_old

def potencia_inversa(A, v0, e):
    A_inv = calcular_inversa(A)
    y_dom, x_dom = metodo_potencia_regular(A_inv, v0, e)
    yn = 1 / y_dom
    xn = x_dom
    return yn, xn

def potencia_deslocamento(A, v0, e, u):
    A_des = [[0.0 for _ in row] for row in A]
    for i in range(len(A)):
        for j in range(len(A)):
            A_des[i][j] = A[i][j]
            if i == j:
                A_des[i][j] -= u
    y_hat, x_hat = potencia_inversa(A_des, v0, e)
    yi = y_hat + u
    xi = x_hat
    return yi, xi


def print_matriz_formatada(M, casas=6, limite_zero=1e-10):
    for linha in M:
        linha_formatada = []
        for valor in linha:
            if abs(valor) < limite_zero:
                linha_formatada.append(0.0)
            else:
                linha_formatada.append(round(float(valor), casas))
        print(linha_formatada)


A = [
    [8, 4, 2, 6, 10],
    [6, 27, 9, 21, 24],
    [4, 12, 44, 24, 16],
    [15, 35, 30, 70, 35],
    [30, 48, 24, 42, 60]
]

B = [
    [2, 0, 0, 0, 0],
    [0, 3, 0, 0, 0],
    [0, 0, 4, 0, 0],
    [0, 0, 0, 5, 0],
    [0, 0, 0, 0, 6]
]


#O problema generalizado Ax = yBx 
#B^-1Ax = yB^-1Bx (B^-1B = I)
#C = B^-1Ax 
# Cx = yx

Binv = [
    [1/2, 0, 0, 0, 0],
    [0, 1/3, 0, 0, 0],
    [0, 0, 1/4, 0, 0],
    [0, 0, 0, 1/5, 0],
    [0, 0, 0, 0, 1/6]
]

c = matriz_matriz(Binv, A)



C = [
    [4, 2, 1, 3, 5],
    [2, 9, 3, 7, 8],
    [1, 3, 11, 6, 4],
    [3, 7, 6, 14, 7],
    [5, 8, 4, 7, 10]
]

v0 = [1, 1, 1, 1, 1]
e = 1e-6


#regular
y1, x1 =  metodo_potencia_regular(c, v0, e)
print("Potencia regular")
print(f"Autovalor: {y1}\nAutovetores: {x1}")

#inversa
yn, xn = potencia_inversa(c, v0, e)
print("Potencia inversa")
print(f"Autovalor: {yn}\nAutovetores: {xn}")

#deslocamento com diferentes u
yi, xi = potencia_deslocamento(c, v0, e, 2)
print("Potencia deslocamento u = 2")
print(f"Autovalor: {yi}\nAutovetores: {xi}")

yi2, xi2 = potencia_deslocamento(c, v0, e, 6)
print("Potencia deslocamento u = 6")
print(f"Autovalor: {yi2}\nAutovetores: {xi2}")

yi3, xi3 = potencia_deslocamento(c, v0, e, 2)
print("Potencia deslocamento u = 12")
print(f"Autovalor: {yi3}\nAutovetores: {xi3}")


#Provar a igualdade Ax = yBx
yB = [[0.0 for _ in range(len(B))] for _ in range(len(B))]
Ax = matriz_vetor(A, x1)

for i in range(len(B)):
    for j in range(len(B)):
        yB[i][j] = B[i][j]*y1

yBx = matriz_vetor(yB, x1)

print("Ax")
print(Ax)
print("yBx:")
print(yBx)