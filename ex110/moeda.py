"""
Exercício Python 108:

- Adapte o código do desafio #107, criando uma função adicional chamada moeda()
- E deve mostrar os números como um valor monetário formatado em Real Brasileiro

"""


def aumentar(valor_porcentagem=0, preco=0.0, formatado=False):
    resultado = preco + (valor_porcentagem * preco) / 100
    return resultado if formatado is False else moeda(resultado)


def diminuir(porcentagem=0, preco=0.0, formatado=False):
    resultado = preco - (porcentagem * preco) / 100
    return resultado if formatado is False else moeda(resultado)


def dobro(numero=0.0, formatado=False):
    resultado = numero * 2
    return resultado if formatado is False else moeda(resultado)


def metade(numero=0.0, formatado=False):
    resultado = numero / 2
    return resultado if formatado is False else moeda(resultado)


def moeda(preco=0.0,simbolo_moeda="R$"):
    resultado= f'{simbolo_moeda}{preco:.2f}'.replace('.', ',')
    return resultado

# def resumo(preco=0.0, aumento=0, diminuicao=0):
#
#     print(f'Preço analisado: {moeda(preco)}')
#     print(f'Dobro do Preço: {dobro(preco, formatado=True)}')
#     print(f'Metade do Preço: {metade(preco, formatado=True)}')
#     print(f'Aumento de {aumento}% {aumentar(aumento, preco, formatado=True)}')
#     print(f'Diminuição de {diminuicao}% {diminuir(diminuicao, preco, formatado=True)}')

def resumo(preco=0.0, aumento=0, diminuicao=0):
    # Cabeçalho da tabela centralizado
    print('-' * 40)  # Linha pontilhada
    print(f"{'RESUMO DO VALOR':^40}")
    print('-' * 40)  # Linha pontilhada

    # Descrições e valores alinhados
    print(f'Preço analisado:\t {moeda(preco)}')
    print(f'Dobro do Preço:\t\t {dobro(preco, formatado=True)}')
    print(f'Metade do Preço:\t {metade(preco, formatado=True)}')
    print(f'Aumento de {aumento}%:\t\t {aumentar(aumento, preco, formatado=True)}')
    print(f'Diminuição de {diminuicao}%:\t {diminuir(diminuicao, preco, formatado=True)}')
    print('-' * 40)  # Linha pontilhada
