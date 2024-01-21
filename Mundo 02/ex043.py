peso = float(input('Quanto você pesa? kg'))
altura = float(input('Qual sua altura?'))
IMC = peso / (altura * altura)
print('Com peso de {}kg e {}m de altura, seu IMC é de {:.1f}'.format(peso, altura, IMC))
if IMC < 18.5:
    classificacao = 'ABAIXO DO PESO'
elif IMC <= 25:
    classificacao = 'PESO IDEAL'
elif IMC <= 30:
    classificacao = 'SOBREPESO'
elif IMC <= 40:
    classificacao = 'OBESIDADE'
elif IMC > 40:
    classificacao = 'OBESIDADE MÓRBIDA'
print('Com esse IMC você se classifica como {}.'.format(classificacao))
