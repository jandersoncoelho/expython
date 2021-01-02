"""
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER

"""
from datetime import date

ano_nascimento = int(input('Informe o ano de nascimento do participante: ').strip())
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f''' O parcipante tem {idade} anos de idade. A categoria dele para a competição é:
    
    - MIRIM.''')
elif idade <= 14:
    print(f''' O parcipante tem {idade} anos de idade. A categoria dele para a competição é:

        - INFANTIL.''')
elif idade <= 19:
    print(f''' O parcipante tem {idade} anos de idade. A categoria dele para a competição é:

        - JUVENIL.''')
elif idade <= 25:
    print(f''' O parcipante tem {idade} anos de idade. A categoria dele para a competição é:

        - SÊNIOR.''')
elif idade > 25:
    print(f''' O parcipante tem {idade} anos de idade. A categoria dele para a competição é:

        - MASTER.''')

