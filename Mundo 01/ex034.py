s = float(input('Qual seu salário atual?'))
if s > 1250.0:
    a = (s * 10 / 100) + s
else:
    a = (s * 15 / 100) + s
print('Seu salário após o aumento será de {:.2f}'.format(a))
