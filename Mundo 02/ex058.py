from random import randint
computador = randint(0, 10)
print('-=-' * 20)
print('\033[1;35mVAMOS JOGAR? PARA ME VENCER DIGA EM QUE NÚMERO EU PENSEI!\033[m')
print('-=-' * 20)
jogador = int(input('\033[1;35mEM QUAL NÚMERO DE 0 A 10 EU PENSEI?\033[m'))
tentativas = 1
while jogador != computador:
    jogador = int(input('\033[1;35mTENTE MAIS UMA VEZ. EM QUAL NÚMERO DE 0 A 10 EU PENSEI?\033[m'))
    tentativas += 1
    if jogador < computador:
        print('\033[1;35mMAIS... TENTE UM NÚMERO MAIOR.\033[m')
    elif jogador > computador:
        print('\033[1;35mMENOS... TENTE UM NÚMERO MENOR.\033[m')
print('\033[1;35mEU JOGUEI {} E VOCÊ JOGOU {}. PARABÉNS, VOCÊ GANHOU !!!\033[m'.format(computador, jogador))
print('\033[1;35mMAS PARA ISSO FORAM PRECISAS {} TENTATIVAS.\033[m'.format(tentativas))
print('-=-' * 20)
