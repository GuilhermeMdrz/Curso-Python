mil = menor = nmenor = cont = soma = 0
print('-=-' * 10)
print('{:^30}'.format('MERCADINHO IDEAL'))
print('-=-' * 10)
while True:
    nome = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    soma += preço
    cont += 1
    if preço >= 1000:
        mil += 1
    if cont == 1 or preço < menor:
        menor = preço
        nmenor = nome
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]')).strip()[0]
    if continuar in 'Nn':
        break
print('-=-' * 10)
print(f'O total gasto foi de R${soma:.2f}')
print(f'Nessa compra tem {mil:.2f} itens que custam R$1000.00 ou mais.')
print(f'O produto mais barato foi o {nmenor} custando {menor:.2f}')
