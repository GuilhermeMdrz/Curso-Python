num = int(input('Digite um número inteiro:'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('Logo {} é um número primo.'.format(num))
else:
    print('Logo {} não é um número primo.'.format(num))
