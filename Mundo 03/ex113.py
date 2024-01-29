def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('\033[31mErro, digite um número inteiro válido!\033[m')
            continue
        else:
            return n
        
def leiafloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except:
            print('\033[31mErro, digite um número real válido!\033[m')
            continue
        else:
            return n2


n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n1}, e o real foi {n2}!')
