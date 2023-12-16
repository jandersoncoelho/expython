from ex108 import moeda

preco = float(input("Digite o Preço: R$"))
porcentagem = float(input("Digite o acréscimo em %: "))

preco_aumentado = moeda.aumentar(porcentagem, preco)
preco_decontado = moeda.diminuir(porcentagem, preco)
preco_dobro = moeda.dobro(preco)
preco_metade = moeda.metade(preco)

print(f"O aumento de {str(porcentagem).replace(".", ",")}% sobre {moeda.moeda(preco, "US$")} é {moeda.moeda(preco_aumentado)}.")
print(f"O desconto de {str(porcentagem).replace(".", ",")}% sobre {moeda.moeda(preco)} é {moeda.moeda(preco_decontado)}.")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.moeda(preco_dobro)}.")
print(f"A metade de {moeda.moeda(preco)} é {moeda.moeda(preco_metade)}.")