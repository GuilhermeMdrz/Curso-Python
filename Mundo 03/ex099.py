def maior(*num):
    m = cont = 0
    for c in range(0, len(num)):
        if c == 0:
            m = num[c]
        else:
            if num[c] > m:
                m = num[c]
        cont += 1
    print('-=-' * 10)
    print(f'Foram passados {cont} valores.')
    print(f'O maior entre eles foi o {m}')
maior(1, 2, 7, 10, 9)
maior(7, 9, 8, 8, 11)
maior()
