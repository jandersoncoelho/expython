import ex112.utilidadescev.dado as d


def leia_int(mensagem: object = str) -> object:
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


def cabecalho(texto: str) -> object:
    print(f'{linha()}')
    print(texto.center(40))
    print(f'{linha()}')


def menu(lista_menu: list):
    while True:
        cabecalho('MENU PRINCIPAL')
        for item_menu in lista_menu:
            print(item_menu)
        print(f'{linha()}')
        opcoes = (1, 2, 3)
        opcao = leia_int('Digite uma das opções acima: ')
        if opcao in opcoes:
            cabecalho(f'opção {opcoes[opcao - 1]}.'.center(40))
            if opcoes[opcao - 1] == 3:
                break
                print('Você saiu do sistema.')

        else:
            d.mostra_mensagem('A opção digitada não existe!', 'LIGHT_PURPLE')
