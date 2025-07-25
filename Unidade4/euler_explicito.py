import math 

# problema 1:
def dy_dt_1(y):
    return (2.0 / 3.0) * y

def solucao_exata1(y0, t0, t):
    return y0 * math.exp((2.0 / 3.0) * (t - t0))

def euler_explicito_1(atual, delta_t, i):
    t_proximo = atual['t'] + delta_t
    y_proximo = atual['y'] + delta_t * dy_dt_1(atual['y'])
    return {'i': i, 't': t_proximo, 'y': y_proximo}




t0 = 0.0
y0 = 1.0
delta_t = 0.1
passos = 10

estado_atual = {'i': 0, 't': t0, 'y': y0}
print("Problema 1: ")
print("\n")
print("-i----t--------y_Euler------y_Exato-----Erro_Absoluto")
print("\n")
for i in range(passos + 1):
    y_exato = solucao_exata1(y0, t0, estado_atual['t'])
    erro = abs(estado_atual['y'] - y_exato)
    print(f"{estado_atual['i']:2d}  {estado_atual['t']:.4f}   {estado_atual['y']:.8f}   {y_exato:.8f}   {erro:.8f}")
    
    if i < passos:
        estado_atual = euler_explicito_1(estado_atual, delta_t, i + 1)



print("\n" + "="*80 + "\n") 

# Problema de segunda ordem:
def dy_dt_2(k, m, g, v):
    dv = -g - (k / m) * v
    return dv

def solucao_exata2(k, m, g, t, y0):
    fator = m / k
    v = -g * fator + (3 + g * fator) * math.exp(- (k / m) * t)
    y = y0 - g * fator * t - (3 + g * fator) * fator * (math.exp(- (k / m) * t) - 1)
    return (v, y)

def euler_explicito_2(k, m, g, t, v, y, delta_t):
    dv = dy_dt_2(k, m, g, v)
    v_proximo = v + delta_t * dv
    y_proximo = y + delta_t * v
    t_proximo = t + delta_t
    return (t_proximo, v_proximo, y_proximo)


k = 1.0
m = 1.0
g = 9.8
t = 0.0
v = 3.0
y0 = 1.0
y = y0
delta_t = 0.1
passos = 10

print("Problema de Segunda ordem: ")
print("\n")
print("-i-----T--------y_Euler------y_Exato-----Erro_Y------V_Euler------V_Exato------Erro_V")
print("\n")

for i in range(passos + 1):
    v_exato, y_exato = solucao_exata2(k, m, g, t, y0)  
    erro_y = abs(y - y_exato)
    erro_v = abs(v - v_exato)

    print(f"{i:2d}  {t:.4f}   {y:.8f}   {y_exato:.8f}   {erro_y:.6f}   {v:.8f}   {v_exato:.8f}   {erro_v:.6f}")

    if i < passos:
        t, v, y = euler_explicito_2(k, m, g, t, v, y, delta_t)

