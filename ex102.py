'''
Exercício Python 102:

- Crie um programa que tenha uma função fatorial()
- A função conterá dois parâmetros: o primeiro que indique o número a calcular e outro chamado "show", que será um valor
booleano indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
- O parâmetro "show" será opcional na função.
-Crie "docstrings" para quando o usuário digitar a função "help()" saiba como utilizá-la.
-Escreva o código usando a "PEP8" e o "Zen to Python"

'''


def fatorial(numero, show=False):
    """
    Função para calcular o fatorial de um número.

    Args:
    numero (int): O número para o qual o fatorial será calculado.
    show (bool, opcional): Um valor booleano indicando se o processo de cálculo será exibido na tela.

    Returns:
    int: O valor do fatorial.
    """
    resultado = 1
    processo = ""

    for i in range(numero, 0, -1):
        resultado *= i
        if show:
            processo += f"{i} x "

    processo = processo[:-2] if show else "Processo de cálculo oculto."

    if show:
        resultado = f"{numero}! = {processo} = {resultado}"
    else:
        resultado = f"{numero}! = {resultado}"

    return resultado


# Programa Principal
n = int(input("Digite um número para calcular o fatorial: "))
mostrar_processo = input("Deseja mostrar o processo de cálculo? (S/N): ").strip().upper() == "S"
print(fatorial(n, show=mostrar_processo))
# help(fatorial)
