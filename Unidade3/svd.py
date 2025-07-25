import math
import QR

def transposta_nquadrada(A):
    linhas = len(A)
    colunas = len(A[0])
    At = [[0.0 for _ in range(linhas)] for _ in range(colunas)]
    
    for i in range(linhas):
        for j in range(colunas):
            At[j][i] = A[i][j]
    return At

def transposta(A):
    n = len(A)
    return [[A[j][i] for j in range(n)] for i in range(n)]

def multiplica(A, B):
    m_A = len(A)
    n_A = len(A[0])
    m_B = len(B)
    n_B = len(B[0])

    if n_A != m_B:
        raise ValueError("As dimensões das matrizes são incompatíveis para multiplicação.")

    C = [[0.0 for _ in range(n_B)] for _ in range(m_A)] 
    
    for i in range(m_A):
        for j in range(n_B):
            for k in range(n_A): 
                C[i][j] += A[i][k] * B[k][j]
    return C

def print_matriz_formatada(M, casas=6, limite_zero=1e-10):
    for linha in M:
        linha_formatada = []
        for valor in linha:
            if abs(valor) < limite_zero:
                linha_formatada.append(0.0)
            else:
                linha_formatada.append(round(float(valor), casas))
        print(linha_formatada)

m, n = 3, 5
A = [
    [4, 2, 1, 3, 5],
    [2, 9, 3, 7, 8],
    [1, 3, 11, 6, 4]
]

e = 1e-10


AT = transposta_nquadrada(A)
AT_A = multiplica(AT, A)
print("AT_A: ")
print_matriz_formatada(AT_A)


P, lamb = QR.metodoQR(AT_A, e)
print("\nAutovalores de AT_A: ")
print([round(val, 6) for val in lamb]) 
print("\nAutovetores de AT_A: ")
print_matriz_formatada(P)


singular_values = [math.sqrt(max(0.0, val)) for val in lamb]

singular_values.sort(reverse=True) 

d = min(m, n)
sigma = singular_values[:d] 

Sigma = [[0.0 for _ in range(n)] for _ in range(m)] 
for i in range(d):
    Sigma[i][i] = sigma[i]

V = P 


U = [[0.0 for _ in range(m)] for _ in range(d)] 

for i in range(d):
    if sigma[i] > e: 
        v_i = [[V[j][i]] for j in range(n)] 

        temp_vec = multiplica(A, v_i)

        for j in range(m):
            U[j][i] = temp_vec[j][0] / sigma[i]
    

VT = transposta(V) 

# Reconstruir A = U * Sigma * V_t
# U_Sigma = U * Sigma
U_Sigma = multiplica(U, Sigma)

# A_reconstruida = U_Sigma * V_t
A_reconstruida = multiplica(U_Sigma, VT)

print("\nResultados SVD ")
print("Matriz Original A:")
print_matriz_formatada(A)

print("\nMatriz U :")
print_matriz_formatada(U)

print("\nMatriz Sigma :")
print_matriz_formatada(Sigma)

print("\nMatriz V :")
print_matriz_formatada(V) 

print("\nMatriz A Reconstruída (U * Sigma * V_t):")
print_matriz_formatada(A_reconstruida)