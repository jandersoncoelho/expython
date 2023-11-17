'''
Exercício Python 104:

- Crie um programa que tenha a função leiaInt().
- Ela vai funcionar de forma semelhante a função input() do Python.
- A validação para aceitar apenas um valor numérico.
- Exemplo: "n = leiaInt(‘Digite um n: ‘)"

'''


def leiaInt(mensagem: object = str) -> object:
    while True:
        numero = input(mensagem)
        if numero.isnumeric():
            return int(numero)
        else:
            print(f'\033[1;31mERRO! {numero} não é um valor numérico válido. Digite novamente.\033[m')


# Programa Principal
n = leiaInt('Digite um número inteiro: ')
print(f'\033[1;33mVocê acabou de digitar o número inteiro {n}.\033[m')
