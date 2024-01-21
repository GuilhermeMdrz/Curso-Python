import math
a = float(input('Digite o valor do ângulo em questão:'))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(a, s))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(a, c))
print('O ângulo de {} tem a TAMGENTE de {:.2f}.'.format(a, t))
