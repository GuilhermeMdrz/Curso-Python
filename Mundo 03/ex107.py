from ex107M import moeda
num = int(input('Digite um valor: R$'))
print(f'R${num} com um aumento de 10% fica R${moeda.aumento(num, 10)}')
print(f'R${num} com um desconto de 10% fica R${moeda.desconto(num, 10)}')
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'A medade de R${num} é de R${moeda.metade(num)}')
