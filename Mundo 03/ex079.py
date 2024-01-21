lista = list()
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print('Novo número registrado!')
    else:
        print('Número já registrado! Tente outro!')
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
print(f'Você digitou os números {lista}.')
lista.sort()
print(f'Em ordem eles ficam {lista}.')
