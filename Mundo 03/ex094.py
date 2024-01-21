lista = list()
soma = 0
while True:
    dicionário = dict()
    dicionário['nome'] = str(input('Nome: '))
    dicionário['sexo'] = str(input('Sexo: [M/F] '))[0]
    while dicionário['sexo'] not in 'MmFf':
        print('ERRO! Por favor, digite apenas M ou F.')
        dicionário['sexo'] = str(input('Sexo: [M/F] '))[0]
    dicionário['idade'] = int(input('Idade: '))
    soma += dicionário['idade']
    lista.append(dicionário.copy())
    continuar = str(input('Quer continuar? [S/N] '))[0]
    while continuar not in 'SsNn':
        print('ERRO! Responda apenas S ou N')
        continuar = str(input('Quer continuar? [S/N] '))[0]
    if continuar in 'Nn':
        break
média = soma / len(lista)
print('-=-' * 30)
print(f'A) Foram cadastradas {len(lista)} pessoas.')
print(f'B) A média de idade {média} anos.')
print('C) As mulheres cadastradas foram ', end='')
for m in range(0, len(lista)):
    if lista[m]['sexo'] in 'Ff':
        print(lista[m]['nome'], end='. ')
print('\nD) Lista das pessoas que estão acima da média:')
for i in range(0, len(lista)):
    if lista[i]['idade'] > média:
        for k, v in lista[i].items():
            print(f'{k} = {v}; ', end='')
        print()
