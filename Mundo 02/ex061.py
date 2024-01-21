print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
t = p
cont = 1
while cont <= 10:
    print('{} -> '.format(t), end='')
    t += r
    cont += 1
print('FIM')
