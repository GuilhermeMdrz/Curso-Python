princ = [[], []]
temp = 0
for c in range(0, 7):
    temp = (int(input('Digite um número: ')))
    if temp % 2 == 1:
        princ[0].append(temp)
    elif temp % 2 == 0:
        princ[1].append(temp)
princ.sort()
print('-=-' * 20)
print(f'Os valores ÍMPARES digitados foram {princ[0]}.')
print(f'Os valores PARES digitados foram {princ[1]}')
