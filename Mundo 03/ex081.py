lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
print(f'Foram digitados {len(lista)} valores.')
lista.sort(reverse=True)
print(f'Os valores digitados foram {lista}')
if 5 in lista:
    print('O número 5 faz parte da lista.')
else:
    print('O número 5 não faz parte da lista.')
