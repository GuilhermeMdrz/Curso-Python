adultos = homens = mulheres = 0
while True:
    print('-=-' * 10)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-=-' * 10)
    idade = int(input('Idade: '))
    if idade >= 18:  # Quantas pessoas tem 18 anos.
        adultos += 1
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] '))
    if sexo in 'Mm':  # Quantos homens foram cadastrados.
        homens += 1
    if sexo in 'Ff' and idade < 20:  # Quantas mulheres tem menos de 20 anos.
        mulheres += 1
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
print('-=-' * 10)
print('{:^30}'.format('ANÁLISE DE DADOS'))
print('-=-' * 10)
print(f'* Nesse grupo existem {adultos} pessoas com 18 anos ou mais.')
print(f'* Nesse grupo foram cadastrados {homens} homens.')
print(f'* Nesse grupo existem {mulheres} mulheres com menos de 20 anos.')
