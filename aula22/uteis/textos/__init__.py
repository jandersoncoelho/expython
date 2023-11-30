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


def mensagem(titulo: str, cor='END', caixa='', centralizado=False):
    """
   Args:
       titulo: título da mensagem
       cor: nome da cor baseado em um dicionário onde estão listadas os códigos de cores ANSI
       centralizado: Alinhamento do texto. Se for True será centralizado
   Returns:

   """
    if caixa != '' and centralizado == True:
        print(caixa * 30)
        print(cores_ansi[cor] + titulo.center(60) + cores_ansi['END'])
        print(caixa * 30)
    elif caixa != '' and centralizado == False:
        print(caixa * 30)
        print(cores_ansi[cor] + titulo + cores_ansi['END'])
        print(caixa * 30)
    elif caixa == '' and centralizado == False:
        print(cores_ansi[cor] + titulo + cores_ansi['END'])
    else:
        print(cores_ansi[cor] + titulo.center(60) + cores_ansi['END'])