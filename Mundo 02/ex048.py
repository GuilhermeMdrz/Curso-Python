soma = 0
cont = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        cont = cont + 1
        soma = soma + num
print('A soma dos {} valores solicitados é igual a {}.'.format(cont, soma))
