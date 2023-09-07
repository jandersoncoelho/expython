'''
Exercício Python 095:

- Aprimore o desafio 93 para que ele funcione com vários jogadores.
- Inclua-os em uma lista.
- Crie um sistema de visualização de detalhes do aproveitamento de cada
jogador.

'''

time = []  # Lista para armazenar os jogadores

while True:
    jogador = {}  # Dicionário para armazenar os dados de um jogador
    jogador['nome'] = input('Digite o nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    
    gols = []
    for partida in range(1, partidas + 1):
        gols_partida = int(input(f'Quantos gols na partida {partida}? '))
        gols.append(gols_partida)
    
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    time.append(jogador)

    continuar = input('Deseja cadastrar mais um jogador? [S/N]: ').strip().upper()
    while continuar not in ('S', 'N'):
        continuar = input('Opção inválida. Deseja continuar [S/N]: ').strip().upper()
    
    if continuar != 'S':
        break

print('-=' * 30)
print(f'{"No.":<4}{"Nome":<15}{"Gols":<20}{"Total":<10}')
print('-' * 60)

for i, jogador in enumerate(time):
    print(f'{i + 1:<4}{jogador["nome"]:<15}{str(jogador["gols"]):<20}{jogador["total"]:<10}')

while True:
    detalhes = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if detalhes == 999:
        break
    if detalhes < 1 or detalhes > len(time):
        print('Jogador não encontrado. Tente novamente.')
    else:
        jogador = time[detalhes - 1]
        print(f' -- LEVANTAMENTO DO JOGADOR {jogador["nome"]}:')
        for i, gols in enumerate(jogador['gols']):
            print(f'   No jogo {i + 1} fez {gols} gols.')
    
print('<< Volte sempre >>')
