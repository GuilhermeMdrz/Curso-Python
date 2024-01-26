from ex108M import moeda
num = int(input('Digite um valor: R$'))
print(f'{moeda.moeda(num)} com um aumento de 10% fica {moeda.moeda(moeda.aumento(num, 10))}')
print(f'{moeda.moeda(num)} com um desconto de 10% fica {moeda.moeda(moeda.desconto(num, 10))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A medade de {moeda.moeda(num)} é de {moeda.moeda(moeda.metade(num))}')
