import numpy as np
import math
def I(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

def transposta(A):
    n = len(A)
    return [[A[j][i] for j in range(n)] for i in range(n)]

def matriz_matriz(A, B):
    n = len(A)
    C = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def matrizjacobiElemento(A, i, j):
    J = I(len(A))
    e = 1e-6

    if abs(A[i][j]) <= e:
        return J
    
    if abs(A[i][i]-A[j][j]) <= e:
        tetha = np.pi/4
    else:
        tetha = 1/2*math.atan((-2*A[i][j])/(A[i][i] - A[j][j]))
    
    J[i][i] = math.cos(tetha)
    J[j][j] = math.cos(tetha)
    J[i][j] = math.sin(tetha)
    J[j][i] = -(math.sin(tetha))

    return J

def varreduraDeJacobi(A, epsilon=1e-10, max_iter=100):
    n = len(A)
    it = 0
    erro = float('inf')

    J = I(n)
    A_velha = A.copy()

    while erro > epsilon and it < max_iter:
        erro = 0.0
        for j in range(n - 1):
            for i in range(j + 1, n):
                if abs(A_velha[i][j]) > epsilon:
                    erro += abs(A_velha[i][j])

                    J_ij = matrizjacobiElemento(A_velha, i, j)
                    J_ij_t = transposta(J_ij)

                    aux = matriz_matriz(J_ij_t, A_velha)
                    A_velha = matriz_matriz(aux, J_ij)
                    J = matriz_matriz(J, J_ij)
        it += 1

    return A_velha, J



def print_matriz_formatada(M, casas=6, limite_zero=1e-10):
    for linha in M:
        linha_formatada = []
        for valor in linha:
            if abs(valor) < limite_zero:
                linha_formatada.append(0.0)
            else:
                linha_formatada.append(round(float(valor), casas))
        print(linha_formatada)

