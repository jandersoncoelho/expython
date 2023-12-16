"""
Exercício Python 108:

- Adapte o código do desafio #107, criando uma função adicional chamada moeda()
- E deve mostrar os números como um valor monetário formatado em Real Brasileiro

"""


def aumentar(valor_porcentagem, preco):
    resultado = preco + (valor_porcentagem * preco) / 100
    return resultado


def diminuir(porcentagem=0, preco=0):
    resultado = preco - (porcentagem * preco) / 100
    return resultado


def dobro(numero):
    resultado = numero * 2
    return resultado


def metade(numero):
    resultado = numero / 2
    return resultado


def moeda(preco=0,simbolo_moeda="R$"):
    resultado= f'{simbolo_moeda}{preco:8.2f}'.replace('.', ',')
    return resultado
