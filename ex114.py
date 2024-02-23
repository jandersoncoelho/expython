"""
Exercício Python 114:

- Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

"""
import ex112.utilidadescev.dado as d
import urllib.request
try:
    url = urllib.request.urlopen("https://pudim.com.br/")
except urllib.error.URLError as e:

    d.mostra_mensagem("URL não acessível no momento!", "RED")
    # print(e.reason)
else:
    d.mostra_mensagem("URL está acessível no momento!", "GREEN")
