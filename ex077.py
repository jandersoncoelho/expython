'''
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

'''
# Criar uma tupla com várias palavras
palavras = ('python', 'programacao', 'computador', 'algoritmo', 'dados', 'gratis')

# Percorrer a tupla e mostrar as vogais de cada palavra
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print(f'\n')
