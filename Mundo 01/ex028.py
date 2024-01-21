from random import choice
n = [0, 1, 2, 3, 4, 5,]
v = choice(n)
r = int(input('Para vencer diga qual número de 0 a 5, o computador escolheu:'))
if r == v:
    print('Parabéns, você ganhou!')
else:
    print('Que pena! o computador ganhou, ele pensou no número {}.'.format(v))
