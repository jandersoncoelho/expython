from ex107 import moeda

preco = float(input("Digite o Preço: R$"))
porcentagem = float(input("Digite o acréscimo em %: "))

preco_aumentado = moeda.aumentar(porcentagem, preco)
preco_decontado = moeda.diminuir(porcentagem, preco)
preco_dobro = moeda.dobro(preco)
preco_metade = moeda.metade(preco)

print(f"O aumento de {porcentagem}% sobre R${preco} é R${preco_aumentado}.")
print(f"O desconto de {porcentagem}% sobre R${preco} é R${preco_decontado}.")
print(f"O dobro de R${preco} é R${preco_dobro}.")
print(f"A metade de R${preco} é R${preco_metade}.")