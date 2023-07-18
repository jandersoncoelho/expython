'''

Exercício Python 089:

- Crie um programa que leia nome e duas notas de vários alunos.

- Coloque o nome e as notas em uma lista.

- Guarde tudo em uma outra lista simulando um diário.

- No final, mostre um boletim em forma de tabela contendo o nome do aluno, as duas notas e a média de cada um.

- Permita que o usuário mostre o boletim de cada aluno individualmente.

- pergunte se deseja ver outro boletim até o final da lista.


'''
diario = []

while True:
    aluno = []  # Lista que representa um aluno

    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    aluno.append(media)

    diario.append(aluno)

    resposta = input("Deseja adicionar outro aluno? [S/N] ").strip().upper()
    if resposta != "S":
        break

print("\nBoletim dos alunos:")
print("=" * 50)
print(f"{'Nome':<20}{'Média':<10}")
print("-" * 50)

for aluno in diario:
    nome = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]
    media = aluno[3]
    print(f"{nome:<20}{media:<10}")

print("=" * 50)

while True:
    opcao = input("\nDeseja ver o boletim de algum aluno? [S/N] ").strip().upper()
    if opcao == "S":
        aluno_desejado = input("Digite o nome do aluno desejado: ")
        encontrado = False
        for aluno in diario:
            if aluno[0] == aluno_desejado:
                nome = aluno[0]
                nota1 = aluno[1]
                nota2 = aluno[2]
##                media = aluno[3]
                print("\nBoletim do aluno:")
                print("=" * 50)
                print(f"{'Nome':<20}{'Nota 1':<10}{'Nota 2':<10}")
                print("-" * 50)
                print(f"{nome:<20}{nota1:<10}{nota2:<10}")
                print("=" * 50)
                encontrado = True
                break
        if not encontrado:
            print("\nAluno não encontrado!")
    else:
        break


print("Fim do programa.")
