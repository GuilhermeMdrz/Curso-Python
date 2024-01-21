print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
t = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(t), end='')
        t += r
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer ver a mais? '))
print('Fim')
print('Progresão finalizada com {} termos.'.format(total))
