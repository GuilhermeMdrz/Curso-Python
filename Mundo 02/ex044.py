inicial = float(input('Qual o valor da compra? R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista cheque/dinheiro.
[ 2 ] à vista no cartão.
[ 3 ] 2x no cartão.
[ 4 ] 3x ou mais no cartão''')
forma = int(input('Qual a forma de pagamento?'))
if forma == 1:
    final = inicial - inicial * 10 / 100
elif forma == 2:
    final = inicial - inicial * 5 / 100
elif forma == 3:
    final = inicial / 2
    print('Sua compra será parcelada em {}x de R${} sem juros'.format(forma, final))
elif forma == 4:
    pergunta = int(input('Em quantas parcelas?'))
    final = inicial + (inicial * 20 / 100)
    parcelado = final / pergunta
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(pergunta, parcelado))
else:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE.')
print('O valor final desse produto será de R${:.2f}'.format(final))
