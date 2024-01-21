altura = float(input('Digite a altura da sua parede:'))
largura = float(input('Didite a largura da sua parede:'))
área = altura * largura
print('\033[1;36mEssa parede tem dimensões de {}x{} e uma área de {}m.\033[m'.format(altura, largura, área))
print('\033[1;36mPara pintar essa parede serão necessários {:.2f} litros de tinta.\033[m'.format(área/2))
