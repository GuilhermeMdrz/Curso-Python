frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range((len(junto) - 1), -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A frase {} É UM PALÍNDROMO !'.format(junto))
elif inverso != junto:
    print('A frase {} NÃO É UM PALÍNDROMO !'.format(junto))
print('Pois seu inverso é {}'.format(inverso))
