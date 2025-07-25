import math
import numpy as np
import jacobi 
e = 1e-6

def matriz_matriz(A, B):
    n = len(A)
    C = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def somaAbaixoDiagonal(A):
    C = 0
    n = len(A)
    for i in range(1, n):
        for j in range(i):
            C += A[i][j]*A[i][j]
    return C

def matrizjacobielementoRvelha(A, i, j, e):
    n = len(A)
    J = jacobi.I(n)
    if abs(A[i][j]) <= e:
        return J
    if abs(A[j][j]) <= e:
        if A[i][j] < 0:
            tetha = math.pi/2
        else:
            tetha = -(math.pi/2)
    else:
        tetha = math.atan(-(A[i][j])/A[j][j])
    J[i][i] = math.cos(tetha)
    J[j][j] = math.cos(tetha)
    J[i][j] = math.sin(tetha)
    J[j][i] = -(math.sin(tetha))

    return J

def decomposicaoQR(A):
    n = len(A)
    QT = jacobi.I(n)
    Rvelha = A
    for j in range(n - 1):
        for i in range(j + 1, n):
            J = matrizjacobielementoRvelha(Rvelha, i, j, e)
            Rnova = jacobi.matriz_matriz(J, Rvelha)
            Rvelha = Rnova
            QTt = jacobi.matriz_matriz(J, QT)
            QT = QTt
    Q = jacobi.transposta(QT)
    R = Rnova
    return Q, R

def metodoQR(A, e):
    n = len(A)
    P = jacobi.I(n)
    Avelha = A
    val = 100
    while val > e:
        Q, R = decomposicaoQR(Avelha)
        Anova = jacobi.matriz_matriz(R, Q)
        Avelha = Anova
        P = jacobi.matriz_matriz(P, Q)
        val = somaAbaixoDiagonal(Anova)
    lamb = [0.0 for _ in range(len(A))]
    for i in range(n):
        lamb[i] = Anova[i][i]
    return P, lamb


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



P, lamb = metodoQR(c, e)


print("Autovalores: ")
print_vetor_formatada(lamb)

print("autovetores: ")
print_matriz_formatada(P)