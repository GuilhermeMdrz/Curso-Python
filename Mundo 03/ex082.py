ambos = list()
p = list()
i = list()
while True:
    ambos.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
for c in ambos:
    if c % 2 == 0:
        p.append(c)
    else:
        i.append(c)
print(f'Você digitou os números {ambos}.')
print(f'Dentre esses os números pares são {p}.')
print(f'E os números ímpares são {i}.')
