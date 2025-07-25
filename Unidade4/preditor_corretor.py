import math

def resolver_edo_primeira_ordem():
    """Resolve a EDO de primeira ordem dy/dt = (2/3)y usando RK4 e preditor-corretor"""
    
    def derivada(t, y):
        return (2.0 / 3.0) * y

    def solucao_exata(y0, t):
        return y0 * math.exp((2.0 / 3.0) * t)

    def passo_rk4(t, y, dt):
        k1 = derivada(t, y)
        k2 = derivada(t + dt/2, y + dt*k1/2)
        k3 = derivada(t + dt/2, y + dt*k2/2)
        k4 = derivada(t + dt, y + dt*k3)
        return y + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)

    # Parâmetros da simulação
    dt = 0.1
    passos = 20
    y0 = 1.0

    # Inicialização dos vetores
    tempo = [0.0] * (passos + 4)
    solucao = [0.0] * (passos + 4)

    # Condições iniciais
    tempo[0] = 0.0
    solucao[0] = y0

    # Runge-Kutta para os primeiros passos
    for i in range(1, 4):
        tempo[i] = tempo[i-1] + dt
        solucao[i] = passo_rk4(tempo[i-1], solucao[i-1], dt)

    print("\nSolução da EDO de Primeira Ordem:")
    print(" i   t       y          y_exato     erro")
    print("----------------------------------------")
    for i in range(4):
        exato = solucao_exata(y0, tempo[i])
        erro = abs(solucao[i] - exato)
        print(f"{i:2d}  {tempo[i]:.2f}  {solucao[i]:.8f}  {exato:.8f}  {erro:.8f}")

    # Método preditor-corretor
    for i in range(4, passos + 1):
        tempo[i] = tempo[i-1] + dt

        # Derivadas anteriores
        derivadas = [derivada(tempo[i-j], solucao[i-j]) for j in range(1, 5)]

        # Predição (Adams-Bashforth)
        predicao = solucao[i-1] + dt/24 * (55*derivadas[0] - 59*derivadas[1] + 37*derivadas[2] - 9*derivadas[3])

        # Correção (Adams-Moulton)
        solucao[i] = solucao[i-1] + dt/24 * (9*derivada(tempo[i], predicao) + 19*derivadas[0] - 5*derivadas[1] + derivadas[2])

        exato = solucao_exata(y0, tempo[i])
        erro = abs(solucao[i] - exato)
        print(f"{i:2d}  {tempo[i]:.2f}  {solucao[i]:.8f}  {exato:.8f}  {erro:.8f}")

def resolver_edo_segunda_ordem():
    """Resolve o sistema de EDOs de segunda ordem usando RK4 e preditor-corretor"""
    
    def derivada_velocidade(k, m, g, v):
        return -g - (k/m) * v

    def derivada_posicao(v):
        return v

    def solucao_exata(t, y0, k, m, g):
        fator = m/k
        termo_exp = math.exp(-(k/m) * t)
        velocidade = -g * fator + (3 + g*fator) * termo_exp
        posicao = y0 - g*fator*t - (3 + g*fator)*fator*(termo_exp - 1)
        return posicao, velocidade

    def passo_rk4(t, y, v, dt, g, k, m):
        # Coeficientes k1
        k1v = derivada_velocidade(k, m, g, v)
        k1y = derivada_posicao(v)
        
        # Coeficientes k2
        v2 = v + dt * k1v / 2
        k2v = derivada_velocidade(k, m, g, v2)
        k2y = derivada_posicao(v2)
        
        # Coeficientes k3
        v3 = v + dt * k2v / 2
        k3v = derivada_velocidade(k, m, g, v3)
        k3y = derivada_posicao(v3)
        
        # Coeficientes k4
        v4 = v + dt * k3v
        k4v = derivada_velocidade(k, m, g, v4)
        k4y = derivada_posicao(v4)
        
        # Atualização
        v_prox = v + (dt/6) * (k1v + 2*k2v + 2*k3v + k4v)
        y_prox = y + (dt/6) * (k1y + 2*k2y + 2*k3y + k4y)
        return y_prox, v_prox

    # Parâmetros da simulação
    g = 9.8
    k = 1.0
    m = 1.0
    dt = 0.1
    passos = 20
    y0 = 150.0
    v0 = 3.0

    # Inicialização dos vetores
    tempo = [0.0] * (passos + 4)
    posicao = [0.0] * (passos + 4)
    velocidade = [0.0] * (passos + 4)

    # Condições iniciais
    tempo[0] = 0.0
    posicao[0] = y0
    velocidade[0] = v0

    # Runge-Kutta para os primeiros passos
    for i in range(1, 4):
        tempo[i] = tempo[i-1] + dt
        posicao[i], velocidade[i] = passo_rk4(tempo[i-1], posicao[i-1], velocidade[i-1], dt, g, k, m)

    print("\nSolução da EDO de Segunda Ordem:")
    print(" i   t       y         y_exato    erro(y)   v        v_exato    erro(v)")
    for i in range(4):
        y_ex, v_ex = solucao_exata(tempo[i], y0, k, m, g)
        erro_y = abs(posicao[i] - y_ex)
        erro_v = abs(velocidade[i] - v_ex)
        print(f"{i:2d}  {tempo[i]:.2f}  {posicao[i]:.6f}  {y_ex:.6f}  {erro_y:.6f}  "
              f"{velocidade[i]:.6f}  {v_ex:.6f}  {erro_v:.6f}")

    # Método preditor-corretor
    for i in range(4, passos + 1):
        tempo[i] = tempo[i-1] + dt

        # Derivadas anteriores
        derivadas_v = [derivada_velocidade(k, m, g, velocidade[j]) for j in range(i-4, i)]
        derivadas_y = [derivada_posicao(velocidade[j]) for j in range(i-4, i)]

        # Predição
        v_pred = velocidade[i-1] + dt/24 * (55*derivadas_v[3] - 59*derivadas_v[2] + 37*derivadas_v[1] - 9*derivadas_v[0])
        y_pred = posicao[i-1] + dt/24 * (55*derivadas_y[3] - 59*derivadas_y[2] + 37*derivadas_y[1] - 9*derivadas_y[0])

        # Correção
        velocidade[i] = velocidade[i-1] + dt/24 * (9*derivada_velocidade(k, m, g, v_pred) + 19*derivadas_v[3] - 5*derivadas_v[2] + derivadas_v[1])
        posicao[i] = posicao[i-1] + dt/24 * (9*derivada_posicao(v_pred) + 19*derivadas_y[3] - 5*derivadas_y[2] + derivadas_y[1])

        y_ex, v_ex = solucao_exata(tempo[i], y0, k, m, g)
        erro_y = abs(posicao[i] - y_ex)
        erro_v = abs(velocidade[i] - v_ex)
        print(f"{i:2d}  {tempo[i]:.2f}  {posicao[i]:.6f}  {y_ex:.6f}  {erro_y:.6f}  "
              f"{velocidade[i]:.6f}  {v_ex:.6f}  {erro_v:.6f}")

if __name__ == "__main__":
    resolver_edo_primeira_ordem()
    resolver_edo_segunda_ordem()