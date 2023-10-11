'''
Exercício Python 101:

-Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa.
-retorne um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
-Crie "docstrings" para quando o usuário digitar a função "help()" saiba como utilizá-la.
- Escreva o código usando a "PEP8" e o "Zen to Python"

'''




def voto(ano_nascimento):
    """
    Função para determinar o direito de voto com base no ano de nascimento.

    Args:
    ano_nascimento (int): O ano de nascimento da pessoa.

    Returns:
    str: Uma string indicando se o voto é NEGADO, OPCIONAL ou OBRIGATÓRIO.
    idade: um valor inteiro indicando a idade calculada a partir do ano de nascimento da pessoa.

    """
    from datetime import date
    ano_atual = date.today().year
    idade_pessoa = ano_atual - ano_nascimento

    if idade_pessoa < 16:
        return idade_pessoa, "VOTO NEGADO"
    elif 16 <= idade_pessoa < 18 or idade_pessoa >= 70:
        return idade_pessoa, "VOTO OPCIONAL"
    else:
        return idade_pessoa, "VOTO OBRIGATÓRIO"


# Exemplo de uso da função
ano = int(input("Digite o ano de nascimento: "))
idade = voto(ano)[0]
resultado = voto(ano)[1]
print(f"Você tem {idade} anos de idade. Seu direito de voto é: {resultado}")
# print(help(voto))
