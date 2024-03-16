from typing import TextIO


def arquivo_existe(nome_arquivo: str):
    try:
        _: TextIO = open(nome_arquivo, 'rt')
        _.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome_arquivo: str):

    # try:
    #     a = open(nome_arquivo, 'w+')
    #     a.close()
    # except Exception as e:
    #     print(f'Erro ao criar o arquivo {nome_arquivo}: {e}')
    # else:
    #     print(f'O arquivo {nome_arquivo} foi criado com sucesso!')

    import os

    # Nome do arquivo a ser criado ou verificado
    nome_do_arquivo = 'meu_arquivo.txt'

    try:
        # Verifica se o arquivo já existe
        if not os.path.exists(nome_do_arquivo):
            print(f'O arquivo {nome_do_arquivo} não existe. Criando um novo arquivo...')
            # Cria um novo arquivo pois ele não existe
            with open(nome_do_arquivo, 'w') as arquivo:
                arquivo.write('Este é um novo arquivo criado pelo script Python.\n')
        else:
            print(f'O arquivo {nome_do_arquivo} já existe.')

        # Abre o arquivo para leitura e escrita ('r+')
        with open(nome_do_arquivo, 'r+') as arquivo:
            # Lê o conteúdo existente
            conteudo = arquivo.read()
            print('Conteúdo atual do arquivo:')
            print(conteudo)

            # Escreve uma nova linha no arquivo
            arquivo.write('Adicionando uma nova linha ao arquivo.\n')

    except FileNotFoundError:
        print('Erro: O arquivo não foi encontrado.')
    except PermissionError:
        print('Erro: Permissão negada para acessar o arquivo.')
    except IsADirectoryError:
        print('Erro: O caminho especificado é um diretório, não um arquivo.')
    except Exception as e:
        print(f'Um erro inesperado ocorreu: {e}')

    print('Operação concluída.')
