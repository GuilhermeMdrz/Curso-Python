menor = 0
maior = 0
for p in range(1, 6):
    peso = float(input('Qual o peso da {} pessoa?'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MENOR peso lido foi {}Kg.'.format(menor))
print('O MAIOR peso lido foi {}Kg.'.format(maior))
