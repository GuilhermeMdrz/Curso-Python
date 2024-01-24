def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else: 
            print('\033[31mErro, digite um número válido!\033[m')
        if ok == True:
            break
    print(f'Você digitou o número {valor}')
n = leiaint('Digite um número: ')
