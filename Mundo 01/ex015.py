km = float(input('Quantos km foram percorridos?'))
d = int(input('Por quantos dias o carro foi alugado?'))
v = (km * 0.15) + (d * 60)
print('O valor a ser pago por alugar esse carro por {} dias e rodar {}km, é de R${}'.format(d, km, v))
