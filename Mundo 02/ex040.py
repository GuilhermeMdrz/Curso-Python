n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
print('Tirando {} e {} sua média foi {}'.format(n1, n2, m))
if m < 5.0:
    print('Você foi REPROVADO !')
elif m <= 6.9:
    print('Você está em RECUPERAÇÃO !')
elif m >= 7.0:
    print('Você foi APROVADO !')
