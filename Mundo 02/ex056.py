media = 0
velho = 0
nomevelho = ''
sexo = 0
cont = 0
for c in range(1, 5):
    print('-----Pessoa {}-----'.format(c))
    nome = str(input('Nome: ')).split()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo m/f: ')).upper().strip()
    media += idade  # Soma da média
    if sexo == 'M':
        if c == 1:  # Idade do homem mais velho.
            velho = idade
            nomevelho = nome
        if idade > velho:
            velho = idade
            nomevelho = nome
    if sexo == 'F':  # Contagem de mulheres < 20.
        if idade < 20:
            cont += 1
print('A idade média desse grupo é de {} anos.'.format(media / 4))  # Média final
print('O homem mais velho desse grupo tem {} anos e se chama {}.'.format(velho, nomevelho))
print('Nesse grupo existem {} mulheres com menos de 20 anos.'.format(cont))
