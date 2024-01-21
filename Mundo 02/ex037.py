n = int(input('Digite um número inteiro:'))
print('Escolha uma base de conversão...')
print('( 1 ) para converter para BINÁRIO.')
print('( 2 ) para converter para OCTAL.')
print('( 3 ) para converter para HEXADECIMAL.')
o = int(input('Digite sua opção:'))
if o == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n[2:])))
elif o == 2:
    print('{} convertido para OCTAl é igual a {}'.format(n, oct(n)[2:]))
elif o == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('{} não é uma opção escolha outra'.format(n))
