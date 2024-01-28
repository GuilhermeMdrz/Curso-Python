def aumento(num=0, aumento=0, formato=False):
    r = num + ((num * aumento) / 100)
    return r if formato == False else moeda(r)

def desconto(num=0, desconto=0, formato=False):
    r = num - ((num * desconto) / 100)
    return r if formato == False else moeda(r)

def dobro(num=0, formato=False):
    r = num * 2
    return r if formato == False else moeda(r)

def metade(num=0, formato=False):
    r = num / 2
    return r if formato == False else moeda(r)

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')

def resumo(num=0, taxaa=10, taxad=10):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço analisado:":20} {moeda(num)}')
    print(f'{"Dobro do preço:":20} {dobro(num, True)}')
    print(f'{"Metade do preço:":20} {metade(num, True)}')
    print(f'{"Ápos aumento:":20} {aumento(num, taxaa, True)}')
    print(f'{"Ápos desconto:":20} {desconto(num, taxad, True)}')
    print('-' * 30)