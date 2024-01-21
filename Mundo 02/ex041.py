from datetime import date
nascimento = int(input('Digite o ano do nascimento:'))
ano = date.today().year
idade = ano - nascimento
if idade <= 9:
    v = 'MIRIM'
elif idade <= 14:
    v = 'INFANTIL'
elif idade <= 19:
    v = 'JÚNIOR'
elif idade <= 25:
    v = 'SÊNIOR'
else:
    v = 'MASTER'
print('Esse atleta tem {} anos, e classifica-se como {}.'.format(idade, v))
