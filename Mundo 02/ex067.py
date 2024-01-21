num = 0
while True:
    num = int(input('Digite um número para ver sua tabuada:'))
    if num <= -1:
        break
    print('~' * 11)
    print(f'''{num} x 1 = {num}
{num} x 2 = {num * 2}
{num} x 3 = {num * 3}
{num} x 4 = {num * 4}
{num} x 5 = {num * 5}
{num} x 6 = {num * 6}
{num} x 7 = {num * 7}
{num} x 8 = {num * 8}
{num} x 9 = {num * 9}''')
    print('~' * 11)
