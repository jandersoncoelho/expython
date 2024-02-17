# """ ANSI color codes """
def altera_cor_texto(nome_cor: str = 'END') -> str:
    """
    Função para alterar a cor do texto na saída do console usando códigos ANSI.

    Parâmetros:
        - nome_cor (str): O nome da cor desejada. Pode ser uma das seguintes opções:
            'BLACK', 'RED', 'GREEN', 'BROWN', 'BLUE', 'PURPLE', 'CYAN', 'LIGHT_GRAY',
            'DARK_GRAY', 'LIGHT_RED', 'LIGHT_GREEN', 'YELLOW', 'LIGHT_BLUE',
            'LIGHT_PURPLE', 'LIGHT_CYAN', 'LIGHT_WHITE', 'BOLD', 'FAINT', 'ITALIC',
            'UNDERLINE', 'BLINK', 'NEGATIVE', 'CROSSED', 'END'.

    Retorna:
        str: O código ANSI correspondente à cor escolhida.

    Exemplo de Uso:
        >>> texto_colorido = f"{altera_cor_texto('RED')}Este texto está em vermelho.{altera_cor_texto()}"
        >>> print(texto_colorido)

    Cores Suportadas:
        - 'BLACK': Preto
        - 'RED': Vermelho
        - 'GREEN': Verde
        - 'BROWN': Marrom
        - 'BLUE': Azul
        - 'PURPLE': Roxo
        - 'CYAN': Ciano
        - 'LIGHT_GRAY': Cinza Claro
        - 'DARK_GRAY': Cinza Escuro
        - 'LIGHT_RED': Vermelho Claro
        - 'LIGHT_GREEN': Verde Claro
        - 'YELLOW': Amarelo
        - 'LIGHT_BLUE': Azul Claro
        - 'LIGHT_PURPLE': Roxo Claro
        - 'LIGHT_CYAN': Ciano Claro
        - 'LIGHT_WHITE': Branco
        - 'BOLD': Negrito
        - 'FAINT': Fraco
        - 'ITALIC': Itálico
        - 'UNDERLINE': Sublinhado
        - 'BLINK': Piscante
        - 'NEGATIVE': Negativo (inversão de cores)
        - 'CROSSED': Tachado
        - 'END': Finaliza a formatação, voltando às configurações padrão.

    Observações: Certifique-se de usar o código 'END' ao final do texto para evitar que a formatação afete o restante
    do conteúdo.

    """
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
    return cores_ansi.get(nome_cor.upper(), 'Cor não suportada')


def leia_dinheiro(mensagem):
    while True:
        valor = input(mensagem).replace(',', '.')  # Substitua ',' por '.' para permitir entrada com '.' ou ','

        # Verifique se o valor contém apenas números e no máximo um ponto decimal
        if valor.replace('.', '').isdigit() and valor.count('.') <= 1:
            return float(valor)  # Converta o valor para float e retorne se for válido
        else:
            print(
                f'{altera_cor_texto('RED')}ERRO! "{valor}" não é um valor monetário válido. Digite novamente.{altera_cor_texto()}')
