d = float(input('Qual é a distância da viagem em questão?'))
if d <= 200:
    print('O valor da passagem para essa viagem de {}Km, é de R${:.2f}'.format(d, d * 0.5))
else:
    print('O valor da passagem para essa viagem de {}km é de R${:.2f}'.format(d, d * 0.45))
