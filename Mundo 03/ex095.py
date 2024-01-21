time = list()
tot = 0
while True:
    gols = list()
    jogador = dict()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        gol = int(input(f'Quantos gols na partida {c + 1}? '))
        tot += gol
        gols.append(gol)
    jogador['gols'] = gols[:]
    jogador['total'] = tot
    time.append(jogador)
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
print(f'{"cod":4} {"nome":15}{"gols":15}{"total":5}')
print('-' * 40)
for c in range(0, len(time)):
    print(f'{c:4} {time[c]["nome"]:15}{time[c]["gols"]}   {time[c]["total"]}')
print('-' * 40)
while True:
    ver = int(input('Mostrar dados de qual jogador? [999 para]'))
    if ver == 999:
        break
    elif ver >= len(time):
        print('Número de jogador não identificado!')
    else:
        print(f'-- Levantamento do jogador {time[ver]["nome"]} --')
        for i, g in enumerate(time[ver]['gols']):
            print(f'   No jogo {i} fez {g} gols.')
        if ver == 999:
            break
