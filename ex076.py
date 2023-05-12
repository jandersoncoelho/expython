'''
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

'''
# Criar uma tupla com nomes de produtos e preços
produtos = ('Arroz', 10.99, 'Feijão', 7.99, 'Macarrão',
            4.50, 'Leite', 2.99, 'Ovo', 0.50)

# Imprimir a tabela de preços
print('=' * 30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('=' * 30)

for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<20} R${produtos[i+1]:>6.2f}')

print('=' * 30)
