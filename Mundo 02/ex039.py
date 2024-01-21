from datetime import date
nascimento = int(input('Em que ano você nasceu?'))
ano = date.today().year
idade = ano - nascimento
print('Quem nasceu em {} tem {} anos.'.format(nascimento, idade))
if idade < 18:
    print('Faltam {} anos para você se alistar no serviço militar obrigatório'.format(18 - idade))
    print('Seu alistamento será em {}'.format(ano + (18 - idade)))
elif idade == 18:
    print('Está na hora de você se alistar no serviço militar obrigatório.')
    print('Seu alistamento será em {}'.format(ano))
else:
    print('Você atrasou {} anos no alistamento do serviço militar obrigatório.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(ano - (idade - 18)))
