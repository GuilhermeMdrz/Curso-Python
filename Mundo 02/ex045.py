from random import choice
j1 = 'pedra'
j2 = 'papel'
j3 = 'tesoura'
computador = choice([j1, j2, j3])
print('-=-' * 20)
print('{:.^60}'.format('SIMULADOR DE PEDRA, PAPEL OU TESOURA'))
print('-=-' * 20)
print('''\033[1;36mPARA ME ENFRENTAR ESCOLHA UMA DAS OPÇÕES: \033[m
[ 1 ] para PEDRA
[ 2 ] para PAPEL.
[ 3 ] para TESOURA.''')
jogada = int(input('Qual sua jogada?'))
if jogada == 1: # jogador jogou PEDRA
    v = 'pedra'
    if computador == v:
        print('Parece que deu EMPATE !')
    elif computador == j2:
        print('Parece que EU GANHEI !')
    elif computador == j3:
        print('Parece que VOCÊ GANHOU !')
    print('já que eu joguei \033[1;36m{}.\033[m E você \033[1;32m{}.\033[m'.format(computador, v))
elif jogada == 2: # jogador jogou PAPEL
    v = 'papel'
    if computador == v:
        print('Parece que deu EMPATE !')
    elif computador == j3:
        print('Parece que EU GANHEI !')
    elif computador == j1:
        print('Parece que VOCÊ GANHOU !')
    print('já que eu joguei \033[1;36m{}.\033[m E você \033[1;32m{}.\033[m'.format(computador, v))
elif jogada == 3: # jogador jogou TESOURA
    v = 'tesoura'
    if computador == v:
        print('Parece que deu EMPATE !')
    elif computador == j1:
        print('Parece que EU GANHEI !')
    elif computador == j2:
        print('Parece que VOCÊ GANHOU !')
    print('já que eu joguei \033[1;36m{}.\033[m E você \033[1;32m{}.\033[m'.format(computador, v))
else: # jogador jogou ERRADO
    print('ESCOLHA INVÁLIDA ! TENTE NOVAMENTE !')
