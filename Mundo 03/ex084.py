pessoas = []
temp = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    continuar = ' '
    while continuar not in 'SsNn:':
        continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso registrado foi de {mai}kg. ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso registrado foi de {men}Kg. ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
