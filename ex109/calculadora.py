from ex109 import moeda

preco = float(input("Digite o Preço: R$"))
porcentagem = float(input("Digite o acréscimo em %: "))

preco_aumentado = moeda.aumentar(porcentagem, preco, formatado=True)
preco_decontado = moeda.diminuir(porcentagem, preco, formatado=True)
preco_dobro = moeda.dobro(preco, formatado=True)
preco_metade = moeda.metade(preco, formatado=True)

print(f"O aumento de {str(porcentagem).replace(".", ",")}% sobre {moeda.moeda(preco)} é {preco_aumentado}.")
print(f"O desconto de {str(porcentagem).replace(".", ",")}% sobre {moeda.moeda(preco)} é {preco_decontado}.")
print(f"O dobro de {moeda.moeda(preco)} é {preco_dobro}.")
print(f"A metade de {moeda.moeda(preco)} é {preco_metade}.")