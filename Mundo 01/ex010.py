r = float(input('Quantos reais você tem na carteira? R$'))
print('Com R$\033[35m{:.2f}\033[m você pode comprar US$\033[36m{:.2f}\033[m.'.format(r, r/3.27))
