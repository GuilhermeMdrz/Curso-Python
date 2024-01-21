d = dict()
d['nome'] = str(input('Nome: '))
d['média'] = float(input(f'Média de {d["nome"]}: '))
if d['média'] >= 7:
    d['situação'] = 'Aprovado'
elif 5 <= d['média'] <= 7:
    d['situação'] = 'Recuperação'
else:
    d['situação'] = 'Reprovado'
print('-=-' * 30)
for k, v in d.items():
    print(f' - {k} é igual a {v}.')
