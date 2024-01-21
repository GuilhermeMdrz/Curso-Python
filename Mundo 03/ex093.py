rendimento = {'nome': str(input('Nome do jogador: '))}
partidas = int(input(f'Quantas partidas {rendimento["nome"]} jogou? '))
tot = 0
g = []
for c in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {c}? '))
    tot += 0
    g.append(gols)
rendimento['total'] = tot
rendimento['gols'] = g[:]
print('-=-' * 20)
print(rendimento)
print('-=-' * 20)
for k, v in rendimento.items():
    print(f'O campo {k} tem o valor de {v}')
print('-=-' * 20)
print(f'O jogador {rendimento["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'   => Na partida {c}, fez {g[c]} gols.')
print(f'Foi um total de {rendimento["total"]} gols.')
