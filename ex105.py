'''
Exercício Python 105:

Faça um programa que tenha uma função notas().
Ele pode receber várias notas de alunos e vai retornar um dicionário python com as seguintes informações:

– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
- Faça uma docstrings para definição da função

'''


def notas(*notas, situacao_turma=False):
    """

    Função para analisar notas de alunos.

    Args:
    *notas (float): Notas dos alunos.
    situacao (bool, opcional): Indica se deve incluir a situação dos alunos (padrão é False).

    Returns:
    dict: Um dicionário com informações sobre as notas
    """
    boletim = dict()
    boletim["quantidade_notas"] = len(notas)
    boletim["maior_nota"] = max(notas)
    boletim["menor_nota"] = min(notas)
    boletim["media_turma"] = sum(notas) / boletim["quantidade_notas"]
    if situacao_turma:
        if boletim["media_turma"] >= 6.0:
            boletim["situacao_aluno"] = "BOA"
        elif 5 <= boletim["media_turma"] < 6.0:
            boletim["situacao_aluno"] = "REGULAR"
        else:
            boletim["situacao_aluno"] = "RUIM"

    return boletim


# programa principal
boletim_aluno = notas(6.0, 5.0, 5.5, 9.5, situacao_turma=True)
print(boletim_aluno)
print(help(notas))
