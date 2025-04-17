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

def potencia(base, expoente):
    return base ** expoente

def raiz_quadrada(x):
    if x < 0:
        raise ValueError("Número negativo não permitido")
    return x ** 0.5 