matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma0 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição ({l} {c}):'))
        if matriz[l][c] % 2 == 0:
            soma0 += matriz[l][c]
print('-=-' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
soma1 = matriz[0][2] + matriz[1][2] + matriz[2][2]
maior = max(matriz[1])
print('-=-' * 20)
print(f'A soma de todos os valores pares é de {soma0}.')
print(f'A soma dos valores da terceira coluna é de {soma1}.')
print(f'A soma dos valores da segunda linha é de {maior}.')
