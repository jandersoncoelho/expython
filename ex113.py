"""
Exercício Python 113:

- Reescreva a função leiaInt() que fizemos no desafio 104.
- Inclua agora a possibilidade da digitação de um número de tipo inválido.
- Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

"""
import ex112.utilidadescev.dado as d


def leia_int(mensagem: object = str) -> object:
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except (ValueError, TypeError):
            print(f'{d.altera_cor_texto('RED')}ERRO! Digite um valor inteiro válido.{d.altera_cor_texto('END')}')

        except KeyboardInterrupt:
            print(f'{d.altera_cor_texto('YELLOW')}\nPrograma interrompido pelo usuário.{d.altera_cor_texto('END')}')
            exit()


def leia_float(mensagem: object = str) -> object:
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except (ValueError, TypeError):
            print(f'{d.altera_cor_texto('RED')}Erro! Digite um valor real válido.{d.altera_cor_texto('END')}')
        except KeyboardInterrupt:
            print(f'{d.altera_cor_texto('YELLOW')}\nPrograma interrompido pelo usuário.{d.altera_cor_texto('END')}')
            exit()


# Programa Principal
n = leia_int('Digite um número inteiro: ')
r = leia_float('Digite um número real: ')
print(f'{d.altera_cor_texto('GREEN')}O número inteiro {n} e o número real {r} são válidos.')
d.altera_cor_texto('END')
