import numpy as np
import QR

def normal(v):
    c = 0
    for i in range(len(v)):
        c += v[i]*v[i]
        res = np.sqrt(c)
    return res

def I(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

def matriz_matriz(A, B):
    n = len(A)
    C = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def householder(A, H, l):
    W  = [0.0 for _ in range(len(A))]
    W_ = [0.0 for _ in range(len(A))]
    N = [0.0 for _ in range(len(A))]
    n =  [0.0 for _ in range(len(A))]
    e = [0.0 for _ in range(len(A))]
    for i in range(l+1, len(W)):
        W[i] = A[i][l]
    
    norW = normal(W)
    W_[l + 1] = norW

    for i in range(len(N)):
        N[i] = W[i] - W_[i]
    
    norN = normal(N)
    if norN< 1e-10:
        H = I(len(H))
    for i in range(len(n)):
        n[i] = 0 if norN==0 else N[i]/norN

    H = I(len(H))
    for i in range(len(H)):
        for j in range(len(H)):
            H[i][j] -= 2*n[i] * n[j]
    return H

def metodo_householder(A, A_tri, H):
    n = len(A)
    A_ = [row[:] for row in A]
    H_i = [[0.0 for _ in range(n)] for _ in range(n)]
    H = I(len(H))
    for i in range(n - 2):
        H_i = householder(A_, H_i, i)
        res = matriz_matriz(H_i, A_)
        A_tri = matriz_matriz(res, H_i)
        res_H = matriz_matriz(H, H_i)
        H = res_H.copy()
        A_ = A_tri.copy()
    return A_tri, H



def print_matriz_formatada(M, casas=6, limite_zero=1e-10):
    for linha in M:
        linha_formatada = []
        for valor in linha:
            if abs(valor) < limite_zero:
                linha_formatada.append(0.0)
            else:
                linha_formatada.append(round(float(valor), casas))
        print(linha_formatada)

def print_vetor_formatada(M, casas=6, limite_zero=1e-10):
    linha_formatada = []
    for valor in M:
        valor = float(valor)
        if abs(valor) < limite_zero:
            linha_formatada.append(0.0)
        else:
            linha_formatada.append(round(valor, casas))
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

n = len(c)
A_tri = [[0.0 for _ in range(n)] for _ in range(n)]
H = [[0.0 for _ in range(n)] for _ in range(n)]
A_tri, H = metodo_householder(c, A_tri, H)

print("A tridiagonal:")
print_matriz_formatada(A_tri)

print("H: ")
print_matriz_formatada(H)

e = 1e-6

#aplicando QR na matriz triagonal gerada pelo metodo de householder em C
#teremos os autovalores de C
p, yc =  QR.metodoQR(A_tri, e)
print(f"\nautovalores de C:")
print_vetor_formatada(yc)

#os autovetores de C serão H * P
xc = matriz_matriz(H, p)
print(f"\nautovetores de C:")
print_matriz_formatada(xc)