nome = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', ' onze', 'doze',
        'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = 0
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while not 0 <= num <= 20:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {nome[num]}.')
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
