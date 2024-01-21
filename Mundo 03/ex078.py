l = list()
mai = men = 0
for cont in range(0, 5):
    l.append(int(input(f'Digite um número para a posição {cont}: ')))
    if cont == 0:
        mai = men = l[cont]
    else:
        if l[cont] > mai:
            mai = l[cont]
        if l[cont] < men:
            men = l[cont]
print(f'Os valores digitados foram: {l}')
print(f'Dentre eles {mai} foi o maior valor encontrado e está nas posições ', end='')
for i, v in enumerate(l):
    if v == mai:
        print(f'{i}...', end=' ')
print(f'\nDentre eles {men} foi o menor valor encontrado e está nas posições ', end='')
for i, v in enumerate(l):
    if v == men:
        print(f'{i}...', end=' ')
