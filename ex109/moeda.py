"""
Exercício Python 108:

- Adapte o código do desafio #107, criando uma função adicional chamada moeda()
- E deve mostrar os números como um valor monetário formatado em Real Brasileiro

"""


def aumentar(valor_porcentagem=0, preco=0, formatado=False):
    resultado = preco + (valor_porcentagem * preco) / 100
    return resultado if formatado is False else moeda(resultado)


def diminuir(porcentagem=0, preco=0, formatado=False):
    resultado = preco - (porcentagem * preco) / 100
    return resultado if formatado is False else moeda(resultado)


def dobro(numero=0, formatado=False):
    resultado = numero * 2
    return resultado if formatado is False else moeda(resultado)


def metade(numero=0, formatado=False):
    resultado = numero / 2
    return resultado if formatado is False else moeda(resultado)


def moeda(preco=0,simbolo_moeda="R$"):
    resultado= f'{simbolo_moeda}{preco:.2f}'.replace('.', ',')
    return resultado
