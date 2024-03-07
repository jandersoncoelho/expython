from lib import interface
# opcoes = (1, 2, 3)
# while True:
#     print('-' * 40)
#     print('MENU PRINCIPAL'.center(40))
#     print('-' * 40)
#     print('1 - Ver pessoas cadastradas')
#     print('2 - Cadastrar pessoas')
#     print('3 - Sair')
#     print('-' * 40)
#
#     opcao = int(input('Digite uma das opções acima: '))
#
#     if opcao in opcoes:
#         print('-' * 40)
#         print(f'opção {opcoes[opcao - 1]}.'.center(40))
#         print('-' * 40)
#         if opcoes[opcao - 1] == 3:
#             print('Você saiu do sistema.')
#             break

# interface.cabecalho('MENU PRINCIPAL')
interface.menu(['1 - Ver pessoas cadastradas', '2 - Cadastrar pessoas', '3 - Sair'])
