from utilidadescev import dado, moeda

preco = dado.leia_dinheiro('digite um número: R$')
print(dado.altera_cor_texto('BLUE'))
moeda.resumo(preco, 10, 10)
print(dado.altera_cor_texto())
print('FIM')
