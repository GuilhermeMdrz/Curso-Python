from ex109M import moeda
num = int(input('Digite um valor: R$'))
print(f'{moeda.moeda(num)} com um aumento de 10% fica {moeda.aumento(num, 10, True)}')
print(f'{moeda.moeda(num)} com um desconto de 10% fica {moeda.desconto(num, 10, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'A medade de {moeda.moeda(num)} é de {moeda.metade(num, True)}')
