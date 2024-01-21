from time import sleep
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite mais um número inteiro: '))
maior = 0
escolha = 0
while escolha != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar.')
    print('[ 3 ] maior.')
    print('[ 4 ] novos números.')
    print('[ 5 ] sair do programa.')
    escolha = int(input('Qual opção você escolhe?'))
    if escolha == 1:
        print('-=-' * 10)
        print('A soma {} + {} = {}'.format(num1, num2, num1 + num2))
        print('-=-' * 10)
    elif escolha == 2:
        print('-=-' * 10)
        print('A multiplicação {} x {} = {}'.format(num1, num2, num1 * num2))
        print('-=-' * 10)
    elif escolha == 3:
        if num1 > num2:
            maior = num1
        if num2 > maior:
            maior = num2
        print('-=-' * 10)
        print('Comparando {} e {}. O maior número é {}.'.format(num1, num2, maior))
        print('-=-' * 10)
    elif escolha == 4:
        print('-=-' * 10)
        num1 = int(input('Digite um número inteiro: '))
        num2 = int(input('Digite mais um número inteiro: '))
        print('-=-' * 10)
    elif escolha > 5:
        print('Escolha inválida. tente novamente. ')
print('-=-' * 10)
print('FINALIZANDO...')
print('-=-' * 10)
sleep(1)
print('PROGRAMA ENCERRADO.')
