import math

## =============================================
## Problema 1: dy/dt = (2/3)*y
## =============================================

def derivada_pvi1(t, y):
    return (2.0 / 3.0) * y

def solucao_exata_pvi1(y0, t):
    return y0 * math.exp((2.0 / 3.0) * t)

def runge_kutta4_pvi1(t, y, dt):
    k1 = derivada_pvi1(t, y)
    k2 = derivada_pvi1(t + dt/2.0, y + dt*k1/2.0)
    k3 = derivada_pvi1(t + dt/2.0, y + dt*k2/2.0) 
    k4 = derivada_pvi1(t + dt, y + dt*k3)
    return y + (dt/6.0) * (k1 + 2*k2 + 2*k3 + k4)

## =============================================
## Problema 2: Queda com resistência do ar
## =============================================

def solucao_exata_pvi2(t, k, m, g, y0):
    fator = m / k
    termo_exp = math.exp(-(k/m) * t)
    v = -g * fator + (3 + g * fator) * termo_exp
    y = y0 - g * fator * t - (3 + g * fator) * fator * (termo_exp - 1)
    return {'v': v, 'y': y}

def derivada_velocidade(v, g, k, m):
    return -g - (k/m) * v

def derivada_posicao(v):
    return v

def runge_kutta4_pvi2(t, v, y, dt, g, k, m):
    # Coeficientes k1
    k1v = derivada_velocidade(v, g, k, m)
    k1y = derivada_posicao(v)
    
    # Coeficientes k2
    k2v = derivada_velocidade(v + dt*k1v/2.0, g, k, m)
    k2y = derivada_posicao(v + dt*k1v/2.0)
    
    # Coeficientes k3
    k3v = derivada_velocidade(v + dt*k2v/2.0, g, k, m)
    k3y = derivada_posicao(v + dt*k2v/2.0)
    
    # Coeficientes k4
    k4v = derivada_velocidade(v + dt*k3v, g, k, m)
    k4y = derivada_posicao(v + dt*k3v)
    
    # Atualiza velocidade e posição
    novo_v = v + (dt/6.0) * (k1v + 2*k2v + 2*k3v + k4v)
    novo_y = y + (dt/6.0) * (k1y + 2*k2y + 2*k3y + k4y)
    
    return {'t': t + dt, 'v': novo_v, 'y': novo_y}

## =============================================
## Programa Principal
## =============================================

if __name__ == "__main__":
    dt = 0.1
    passos = 10
    
    print("\n=== PVI-1: dy/dt = (2/3)*y ===")
    y0 = 1.0
    y = y0
    
    for i in range(passos + 1):
        t = i * dt
        y_exato = solucao_exata_pvi1(y0, t)
        erro = abs(y - y_exato)
        print(f"t={t:.2f} | y (RK4)={y:.8f} | y (exato)={y_exato:.8f} | erro={erro:.8f}")
        y = runge_kutta4_pvi1(t, y, dt)
    
    print("\n=== PVI-2: Queda com resistência do ar ===")
    g = 9.8
    k = 1.0
    m = 1.0
    estado = {'t': 0.0, 'v': 3.0, 'y': 150.0}
    
    for i in range(passos + 1):
        exato = solucao_exata_pvi2(estado['t'], k, m, g, 150.0)
        erro_v = abs(estado['v'] - exato['v'])
        erro_y = abs(estado['y'] - exato['y'])
        print(f"t={estado['t']:.2f} | v={estado['v']:.6f} (exato={exato['v']:.6f}) | "
              f"y={estado['y']:.6f} (exato={exato['y']:.6f}) | "
              f"erro_v={erro_v:.6f} | erro_y={erro_y:.6f}")
        estado = runge_kutta4_pvi2(estado['t'], estado['v'], estado['y'], dt, g, k, m)