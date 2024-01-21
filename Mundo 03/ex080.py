lista = list()
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[- 1]:
        lista.append(num)
        print('Valor adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Valor adicionado a posição {pos}. ')
                break
            pos += 1
print(lista)
print(f'Os valores ordenados foram {lista}.')
