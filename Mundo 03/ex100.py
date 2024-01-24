from random import randint
número = []
def sorteia(lista):
    print('os valores digitados foram ', end='')
    for c in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        print(f'{num}. ', end='')
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nA soma dos valores pares é de {soma}.')
sorteia(número)
somapar(número)
