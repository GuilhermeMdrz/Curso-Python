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
