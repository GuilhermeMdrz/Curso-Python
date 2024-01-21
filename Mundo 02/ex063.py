print('-=' * 12)
print('SEQUÊNCIA DE FIBONACCI')
print('-=' * 12)
num = int(input('Quantos termos você quer ver? '))
termo1 = 0
termo2 = 1
contador = 3
print('{} -> {} -> '.format(termo1, termo2), end='')
while contador <= num:
    termo3 = termo1 + termo2
    print('{} -> '.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    contador += 1
print('FIM')
