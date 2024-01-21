p = int(input('Primeiro valor:'))
s = int(input('Segundo valor:'))
t = int(input('Terceiro valor:'))
if p < s and p < t:
    menor = p
if s < p and s < t:
    menor = s
if t < p and t < s:
    menor = t
if p > s and p > t:
    maior = p
if s > p and s > t:
    maior = s
if t > p and t > s:
    maior = t
print('O menor valor colocado foi {}.'.format(menor))
print('O maior valor colocado foi {}.'.format(maior))
