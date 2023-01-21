'''
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.

'''

tabela_brasileirao_2017 = ('Corinthians',
                           'Palmeiras',
                           'Santos',
                           'Grêmio',
                           'Cruzeiro',
                           'Flamengo',
                           'Vasco da Gama',
                           'Chapecoense',
                           'Atlético - MG',
                           'Botafogo',
                           'Atlético - PR',
                           'Bahia',
                           'São Paulo',
                           'Fluminense',
                           'Sport - PE',
                           'Vitória - BA',
                           'Coritiba',
                           'Avaí',
                           'Ponte Preta',
                           'Atlético - GO',
                           )

print('=-' * 20)
print('{:-^40}'.format('CLASSIFICAÇÃO BRASILEIRÃO 2017'))
print('=-' * 20)

print(f'Os 5 primeiros times da tabela foram {tabela_brasileirao_2017[0:5]}')
print('=-' * 20)
print(f'Os 4 últimos times da tabela foram {tabela_brasileirao_2017[-4:]}')
print('=-' * 20)
print(f'Os times em ordem alfabética: {sorted(tabela_brasileirao_2017)}')
print('=-' * 20)
print(
    f'A Chapecoense terminou o campeonato na {tabela_brasileirao_2017.index("Chapecoense") + 1}ª posição')
