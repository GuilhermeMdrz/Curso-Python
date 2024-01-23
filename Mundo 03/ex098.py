from time import sleep
def contagem(a, b, c):
    print('-=-' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}.')
    sleep(2.5)
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    if a < b:
        cont =  a
        while cont <= b:
            print(f'{cont} => ', end='', flush=True)
            sleep(0.5)
            cont += c
        print('FIM')
    else:
        cont = a
        while cont >= b:
            print(f'{cont} => ', end='', flush=True)
            sleep(0.5)
            cont -= c
        print('FIM')
contagem(1, 10, 1)
contagem(10, 0, 2)
print('-=-' * 20)
print('Agora crie a sua contagem!')
ini = int(input('Inicio: '))
fim = int(input('Final: '))
pas = int(input('DE quanto em quanto? '))
contagem(ini, fim, pas)
