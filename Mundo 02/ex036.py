valor = float(input('Digite o valor do imóvel em questão: R$'))
salario = float(input('Digite seu salário atual:'))
tempo = int(input('Digite em quantos anos você planeja pagar o imóvel:'))
parcela = valor / (tempo * 12)
teto = (30 * salario) / 100
print('-=-' * 30)
print('Para pagar uma casa de R${:.2f} em {} anos, a parcela corresponde a um valor de R${:.2f}'.format(valor, tempo, parcela))
if parcela > teto:
    print('Sinto muito, seu empréstimo foi \033[1;31mNEGADO\033[m!')
else:
    print('Seu empréstimo foi \033[1;32mAPROVADO\033[m!')
print('Tenha um bom dia!')
print('-=-' * 30)
