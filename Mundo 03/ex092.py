from datetime import date
d = dict()
d['nome'] = str(input('Nome: '))
d['idade'] = date.today().year - int(input('Ano de Nascimento: '))
d['carteira'] = int(input('Carteira de Trabalho (0 não tem) '))
if d['carteira'] != 0:
    d['contratação'] = int(input('Ano de Contratação: '))
    d['salário'] = float(input('Salário: R$'))
    d['aposentadoria'] = d['idade'] + 35
print('-=-' * 30)
for k, v in d.items():
    print(f' - {k} tem o valor {v}')
