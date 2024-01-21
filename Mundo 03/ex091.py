from random import randint
from operator import itemgetter
jogadas = dict()
jogadas['jogador1'] = randint(1, 6)
jogadas['jogador2'] = randint(1, 6)
jogadas['jogador3'] = randint(1, 6)
jogadas['jogador4'] = randint(1, 6)
ranking = list()
for k, v in jogadas.items():
    print(f'{k} tirou {v} no dado.')
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('-=-' * 30)
for i, v in enumerate(ranking):
    print(f' {i + 1}o lugar {v[0]} com {v[1]}')