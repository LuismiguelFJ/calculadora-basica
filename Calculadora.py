def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def mutiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por Zero!")
    return a / b