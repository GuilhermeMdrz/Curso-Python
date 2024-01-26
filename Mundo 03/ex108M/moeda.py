def aumento(num=0, aumento=0):
    r = num + ((num * aumento) / 100)
    return r

def desconto(num=0, desconto=0):
    r = num - ((num * desconto) / 100)
    return r

def dobro(num=0):
    r = num * 2
    return r

def metade(num=0):
    r = num / 2
    return r

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')
