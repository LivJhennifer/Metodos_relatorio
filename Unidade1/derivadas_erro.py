import math

def fun(x):
    return math.sin(x)

#derivada primeira

def derivada_primeira_forward(erro, x, deltax):
    if erro == 1:
        return (fun(x + deltax) - fun(x)) / deltax
    elif erro == 2:
        return (-fun(x + 2*deltax) + 4*fun(x + deltax) - 3*fun(x)) / (2*deltax)
    elif erro == 3:
        return (-11*fun(x) + 18*fun(x + deltax) - 9*fun(x + 2*deltax) + 2*fun(x + 3*deltax)) / (6*deltax)
    elif erro == 4:
        return (-25*fun(x) + 48*fun(x + deltax) - 36*fun(x + 2*deltax) + 16*fun(x + 3*deltax) - 3*fun(x + 4*deltax)) / (12*deltax)
    else:
        print("Ordem de erro invalida")
    

def derivada_primeira_backward(erro, x, deltax):
    if erro == 1:
        return (fun(x) - fun(x - deltax)) / deltax
    elif erro == 2:
        return (3*fun(x) - 4*fun(x - deltax) + fun(x - 2*deltax)) / (2*deltax)
    elif erro == 3:
        return (11*fun(x) - 18*fun(x - deltax) + 9*fun(x - 2*deltax) - 2*fun(x - 3*deltax)) / (6*deltax)
    elif erro == 4:
        return (25*fun(x) - 48*fun(x - deltax) + 36*fun(x - 2*deltax) - 16*fun(x - 3*deltax) + 3*fun(x - 4*deltax)) / (12*deltax)
    else:
        print("Ordem de erro invalida")


def derivada_primeira_central(erro, x, deltax):
    if erro == 2:
        return (fun(x + deltax) - fun(x - deltax)) / (2*deltax)
    elif erro == 4:
        return (-fun(x + 2*deltax) + 8*fun(x + deltax) - 8*fun(x - deltax) + fun(x - 2*deltax)) / (12*deltax)
    else:
        print("Ordem de erro invalida")


#derivada segunda

def derivada_segunda_forward(erro, x, deltax):
    if erro == 1:
        return (fun(x) - 2*fun(x + deltax) + fun(x + 2*deltax)) / (deltax * deltax)
    elif erro == 2:
        return (2*fun(x) - 5*fun(x + deltax) + 4*fun(x + 2*deltax) - fun(x + 3*deltax)) / (deltax * deltax)
    elif erro == 3:
        return (35*fun(x) - 104*fun(x + deltax) + 114*fun(x + 2*deltax) - 56*fun(x + 3*deltax) + 11*fun(x + 4*deltax)) / (12 * deltax * deltax)
    else:
        print("Ordem de erro invalida")


def derivada_segunda_backward(erro, x, deltax):
    if erro == 1:
        return (fun(x) - 2*fun(x - deltax) + fun(x - 2*deltax)) / (deltax * deltax)
    elif erro == 2:
        return (2*fun(x) - 5*fun(x - deltax) + 4*fun(x - 2*deltax) - fun(x - 3*deltax)) / (deltax * deltax)
    elif erro == 3:
        return (35*fun(x) - 104*fun(x - deltax) + 114*fun(x - 2*deltax) - 56*fun(x - 3*deltax) + 11*fun(x - 4*deltax)) / (12 * deltax * deltax)
    else:
        print("Ordem de erro invalida")


def  derivada_segunda_central(erro, x, deltax):
    if erro == 2:
        return (fun(x + deltax) - 2*fun(x) + fun(x - deltax)) / (deltax * deltax)
    elif erro == 4:
        return (-fun(x + 2*deltax) + 16*fun(x + deltax) - 30*fun(x) + 16*fun(x - deltax) - fun(x - 2*deltax)) / (12 * deltax * deltax)
    else: 
        print("Ordem de erro invalida")


# derivada terceira

def derivada_terceira_forward(erro, x, deltax):
    if erro == 1:
        return (fun(x + 3*deltax) - 3*fun(x + 2*deltax) + 3*fun(x + deltax) - fun(x)) / (deltax * deltax * deltax)
    elif erro == 2:
        return (-5*fun(x) + 18*fun(x + deltax) - 24*fun(x + 2*deltax) + 14*fun(x + 3*deltax) - 3*fun(x + 4*deltax)) / (2 * deltax * deltax * deltax)
    else:
        print("Ordem de erro invalida")


def derivada_terceira_backward(erro, x, deltax):
    if erro == 1:
        return (fun(x) - 3*fun(x - deltax) + 3*fun(x - 2*deltax) - fun(x - 3*deltax)) / (deltax * deltax * deltax)
    elif erro == 2:
        return (5*fun(x) - 18*fun(x - deltax) + 24*fun(x - 2*deltax) - 14*fun(x - 3*deltax) + 3*fun(x - 4*deltax)) / (2 * deltax * deltax * deltax)
    else:
        print("Ordem de erro invalida")


def derivada_terceira_central(erro, x, deltax):
    if erro == 2:
        return (fun(x + 2*deltax) - 2*fun(x + deltax) + 2*fun(x - deltax) - fun(x - 2*deltax)) / (2 * deltax * deltax * deltax)
    elif erro == 4:
        return (-fun(x + 3*deltax) + 8*fun(x + 2*deltax) - 13*fun(x + deltax) + 13*fun(x - deltax) - 8*fun(x - 2*deltax) + fun(x - 3*deltax)) / (8 * deltax * deltax * deltax)
    else:
        print("Ordem de erro invalida")





x = int(input("Entre com o valor de x: "))
deltax = int(input("Entre com o valor de DeltaX: "))
ordem = int(input("Entre com a ordem da Derivada: 1 (Primeira), 2(Segunda), 3(Terceira) "))
filosofia = int(input("Entre com a Filosofia: 1 (Forward), 2 (Backward), 3 (Central) "))

if ordem == 1:
    if filosofia == 1:
        erro = int(input("Entre com a ordem do erro: 1 (Linear), 2 (Quadratico), 3 (Cubico), 4 (Ordem quarta) "))
        resultado = derivada_primeira_forward(erro, x, deltax)
    elif filosofia == 2:
        erro = int(input("Entre com a ordem do erro: 1 (Linear), 2 (Quadratico), 3 (Cubico), 4 (Ordem quarta) "))
        resultado = derivada_primeira_backward(erro, x, deltax)
    elif filosofia == 3:
        erro = int(input("Entre com a ordem do erro: 2 (Quadratico), 4 (Ordem quarta) "))
        resultado = derivada_primeira_central(erro, x, deltax)
    else:
        print("Filosofia invalida")
elif ordem == 2:
    if filosofia == 1:
        erro = int(input("Entre com a ordem do erro: 1 (Linear), 2 (Quadratico), 3 (Cubico) "))
        resultado = derivada_segunda_forward(erro, x, deltax)
    elif filosofia == 2:
        erro = int(input("Entre com a ordem do erro: 1 (Linear), 2 (Quadratico), 3 (Cubico) "))
        resultado = derivada_segunda_backward(erro, x, deltax)
    elif filosofia == 3:
        erro = int(input("Entre com a ordem do erro: 2 (Quadratico), 4 (Ordem quarta) "))
        resultado = derivada_segunda_central(erro, x, deltax)
    else:
        print("Filosofia invalida")
elif ordem == 3:
    if filosofia == 1:
        erro = int(input("Entre com a ordem do erro: 1 (Linear), 2 (Quadratico) "))
        resultado = derivada_terceira_forward(erro, x, deltax)
    elif filosofia == 2:
        erro = int(input("Entre com a ordem do erro: 1 (Linear), 2 (Quadratico) "))
        resultado = derivada_terceira_backward(erro, x, deltax)
    elif filosofia == 3:
        erro = int(input("Entre com a ordem do erro: 2 (Quadratico), 4 (Ordem quarta) "))
        resultado = derivada_terceira_central(erro, x, deltax)
else:
    print("Ordem de Derivada invalida")

print(f'O resultado para as entradas de X = {x}, DeltaX = {deltax}, Filosofia = {filosofia} (1 (Forward), 2 (Backward), 3 (Central)), Ordem da Derivada = {ordem} (1 (Primeira), 2(Segunda), 3(Terceira)) e ordem do erro = {erro} (1 (Linear), 2 (Quadratico), 3 (Cubico), 4 (Ordem quarta))\né: {resultado}')