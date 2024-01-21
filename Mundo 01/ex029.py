v = int(input('Qual é a velocidade do carro?'))
m = (v - 80) * 7
if v > 80:
    print('Você está acima da velocidade permitida de 80Km/h')
    print('E acabou de receber uma multa no valor de R${:.2f}'.format(m))
print('Tenha um bom dia e dirija com segurança!')
