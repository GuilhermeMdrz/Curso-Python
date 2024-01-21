cont = soma = media = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número inteiro.'))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
media = soma / cont
print('Você digitou {} números e a média entre eles é de {:.2f}.'.format(cont, media))
print('O maior número digitado foi {} e o menor {}.'.format(maior, menor))
