geral = [[], [], []]
cont = 0
while True:
    nome = str(input('Nome: '))
    geral[0].append(nome)
    nota1 = float(input('Nota 1: '))
    geral[1].append(nota1)
    nota2 = float(input('Nota 2: '))
    geral[2].append(nota2)
    cont += 1
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
print('-=-' * 10)
print(f'{"No."} {"NOME":15}{"MÉDIA"}')
for c in range(0, cont):
    print(f'{c:<3} {geral[0][c]:15}{(geral[1][c] + geral[2][c]) / 2}')
print('-=-' * 10)
while True:
    ver = int(input('Mostrar notas de qual aluno? (999 para) '))
    if ver >= 999:
        break
    print(f'As notas de {geral[0][ver]} são {geral[1][ver]} e {geral[2][ver]}')
    print('-=-' * 10)
