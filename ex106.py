"""
Exercício Python 106:

- Faça um mini-sistema que utilize o Interactive Help do Python.
- O usuário vai digitar o comando e o manual vai aparecer.
- Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
- Importante: use cores.

"""

""" ANSI color codes """
cores_ansi = {
    'BLACK': "\033[0;30m",
    'RED': "\033[0;31m",
    'GREEN': "\033[0;32m",
    'BROWN': "\033[0;33m",
    'BLUE': "\033[0;34m",
    'PURPLE': "\033[0;35m",
    'CYAN': "\033[0;36m",
    'LIGHT_GRAY': "\033[0;37m",
    'DARK_GRAY': "\033[1;30m",
    'LIGHT_RED': "\033[1;31m",
    'LIGHT_GREEN': "\033[1;32m",
    'YELLOW': "\033[1;33m",
    'LIGHT_BLUE': "\033[1;34m",
    'LIGHT_PURPLE': "\033[1;35m",
    'LIGHT_CYAN': "\033[1;36m",
    'LIGHT_WHITE': "\033[1;37m",
    'BOLD': "\033[1m",
    'FAINT': "\033[2m",
    'ITALIC': "\033[3m",
    'UNDERLINE': "\033[4m",
    'BLINK': "\033[5m",
    'NEGATIVE': "\033[7m",
    'CROSSED': "\033[9m",
    'END': "\033[0m"
}


def ajuda_python(comando: str):
    print(cores_ansi['LIGHT_PURPLE'])
    help(comando)
    print(cores_ansi['END'])


def mensagem(titulo: str, cor='END'):
    """
   Args:
       titulo: título da mensagem
       cor: nome da cor baseado em um dicionário onde estão listadas os códigos de cores ANSI

   Returns:

   """
    print('-=' * 30)
    print(cores_ansi[cor] + titulo.center(60) + cores_ansi['END'])
    print('-=' * 30)


while True:
    mensagem('Ajuda do Python', 'RED')
    comando_python = input(
        cores_ansi['BLUE'] + 'Digite um comando em python [Digite FIM PARA ENCERRAR]: ' + cores_ansi['END'])
    if comando_python.upper().strip() == 'FIM':
        break
    else:
        ajuda_python(comando_python)

mensagem('Fim do Programa.', 'YELLOW')
