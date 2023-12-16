def aumentar(valor_porcentagem, preco):
    resultado = preco + (valor_porcentagem * preco) / 100
    return resultado


def diminuir(porcentagem, preco):
    resultado = preco - (porcentagem * preco) / 100
    return resultado


def dobro(numero):
    resultado = numero * 2
    return resultado


def metade(numero):
    resultado = numero / 2
    return resultado
