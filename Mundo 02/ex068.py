from random import randint
print('-=' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('-=' * 30)
cont = 0
while True:
    num1 = int(input('Digite um número: '))
    palpite = str(input('Ímpar ou Par? [I/P] ')).upper()[0]
    num2 = randint(0, 10)
    soma = num1 + num2
    while palpite not in 'PI':
        palpite = str(input('Ímpar ou Par? [I/P] ')).upper()[0]
    if soma % 2 == 0:  # conferir se é par
        vencer = 'P'
        print(f'Eu joguei {num2}, e você {num1}. O número {soma} é PAR')
    else:  # conferir se é ímpar
        vencer = 'I'
        print(f'Eu joguei {num2}, e você {num1}. O número {soma} é ÍMPAR')
    if vencer == palpite:  # se jogador venceu
        print('Você venceu !')
        print('Vamos jogar novamente...')
        cont += 1
    if vencer != palpite:  # se jogador perdeu
        break
print('-=' * 30)
print(f'VOCÊ PERDEU. MAS AINDA ASSIM TEVE {cont} VITÓRIAS CONSECUTIVAS.')
print('-=' * 30)
