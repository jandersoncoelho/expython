from uteis import numeros, textos

numero = int(input("Digite um número: "))
f = numeros.fatorial(numero)
d = numeros.dobro(numero)
t = numeros.triplo(numero)
textos.mensagem(f'O fatorial de {numero} é {f}', "YELLOW", "--", centralizado=True)
textos.mensagem(f'O dobro de {numero} é {d}', "LIGHT_BLUE", caixa='==')
textos.mensagem(f'O triplo de {numero} é {t}',"GREEN",centralizado=True)