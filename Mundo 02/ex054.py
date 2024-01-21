from datetime import date
maior = 0
menor = 0
acumulo = 1
atual = date.today().year
for c in range(1, 7):
    nascimento = int(input(('Em que ano a {} pessoa nasceu?'.format(acumulo))))
    acumulo += 1
    if atual - nascimento == 18 or atual - nascimento > 18:
        maior += 1
    else:
        idade = 'MENOR DE IDADE'
        menor += 1
print('Nesse grupo existem {} pessoas de MENOR, e {} pessoas de MAIOR.'.format(menor, maior))