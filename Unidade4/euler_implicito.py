import math

# === PVI-1: dy/dt = (2/3)*y ===

def euler_implicito_pvi1(y_n, dt):
    return y_n / (1 - (2.0 / 3.0) * dt)

def solucao_exata_pvi1(y0, t):
    return y0 * math.exp((2.0 / 3.0) * t)

# Parâmetros
dt = 0.1
passos = 10
y0 = 2.0
y_n = y0

print("=== PVI-1: dy/dt = (2/3)*y ===")
print(f"{'t':>5} | {'y_implícito':>12} | {'y_exato':>10} | {'erro':>10}")
print("-" * 45)
for i in range(passos + 1):
    t = i * dt
    y_exato = solucao_exata_pvi1(y0, t)
    erro = abs(y_n - y_exato)
    print(f"{t:5.2f} | {y_n:12.6f} | {y_exato:10.6f} | {erro:10.6f}")
    y_n = euler_implicito_pvi1(y_n, dt)


# === PVI-2: Queda com resistência ===

def euler_implicito_pvi2(t_n, v_n, y_n, dt, k, m, g):
    coef = 1 + (k / m) * dt
    v_proximo = (v_n - g * dt) / coef
    y_proximo = y_n + dt * v_proximo
    t_proximo = t_n + dt
    return t_proximo, v_proximo, y_proximo

def solucao_exata_pvi2(t, k, m, g, y0):
    fator = m / k
    v = -g * fator + (3 + g * fator) * math.exp(-(k / m) * t)
    y = y0 - g * fator * t - (3 + g * fator) * fator * (math.exp(-(k / m) * t) - 1)
    return v, y

k = 1.0
m = 1.0
g = 9.8
t = 0.0
v = 3.0
y0 = 150.0
y = y0

print("\n=== PVI-2: Queda com resistência ===")
print(f"{'t':>5} | {'v':>10} | {'v_exato':>10} | {'y':>10} | {'y_exato':>10} | {'erro_v':>10} | {'erro_y':>10}")
print("-" * 80)
for i in range(passos + 1):
    v_exato, y_exato = solucao_exata_pvi2(t, k, m, g, y0)
    erro_v = abs(v - v_exato)
    erro_y = abs(y - y_exato)
    print(f"{t:5.2f} | {v:10.6f} | {v_exato:10.6f} | {y:10.6f} | {y_exato:10.6f} | {erro_v:10.6f} | {erro_y:10.6f}")
    t, v, y = euler_implicito_pvi2(t, v, y, dt, k, m, g)
