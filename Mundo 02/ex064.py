cont = num = soma = 0
while num != 999:
    num = int(input('Digite um número inteiro [999 para parar].'))
    if num != 999:
        soma += num
        cont += 1
print('A soma entre os {} números digitados é {}'.format(cont, soma))
