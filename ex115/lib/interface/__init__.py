from time import sleep

import ex112.utilidadescev.dado as d
from ex115.lib.cadastro_pessoas import *


def leia_int(mensagem: object = str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except (ValueError, TypeError, IndexError):
            print(f'{d.altera_cor_texto('RED')}ERRO! Digite um valor inteiro válido.{d.altera_cor_texto('END')}')

        except KeyboardInterrupt:
            print(f'{d.altera_cor_texto('YELLOW')}\nPrograma interrompido pelo usuário.{d.altera_cor_texto('END')}')
            exit()


def linha(tamanho=40):
    return "*" * tamanho


def cabecalho(texto: str) -> str:
    d.mostra_mensagem(f'{linha()}', 'YELLOW')
    d.mostra_mensagem(texto.center(40), 'BLUE')
    d.mostra_mensagem(f'{linha()}', 'YELLOW')


def menu(lista_menu: list):
    nome_arquivo = 'pessoas.txt'
    if arquivo_existe(nome_arquivo):
        d.mostra_mensagem(f'O arquivo {nome_arquivo} existe.', 'LIGHT_CYAN')
    else:
        d.mostra_mensagem(f'O arquivo {nome_arquivo}  não existe.', 'RED')
        criar_arquivo(nome_arquivo)
    while True:
        cabecalho('MENU PRINCIPAL')
        for item_menu in lista_menu:
            print(item_menu)
        d.mostra_mensagem(f'{linha()}', 'YELLOW')
        opcao: int = leia_int('Digite uma das opções acima: ')
        if opcao == 3:
            cabecalho('Você saiu do sistema.')
            break
        elif opcao == 2:
            cabecalho(lista_menu[opcao - 1])
        elif opcao == 1:
            cabecalho(lista_menu[opcao - 1])


        else:
            d.mostra_mensagem('A opção digitada não existe!', 'LIGHT_PURPLE')
        sleep(2)
