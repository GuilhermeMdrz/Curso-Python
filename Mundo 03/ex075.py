nums = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')), int(input('Digite um último número: ')))
print(f'Os valores digitados foram {nums}.')
a = 0
n = nums.count(9)
if n > 0:
    print(f'O número 9 apareceu {n} vezes.')
if 3 in nums:
    print(f'O número 3 foi digitado pela primeira vez na {nums.index(3) + 1} posição.')
else:
    print('O número 3 não foi digitado.')
print('Os valores pares digitados foram: ', end='')
for a in nums:
    if a % 2 == 0:
        print(a, end=' ')
