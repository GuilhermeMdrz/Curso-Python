from ex111M import dados, moeda
def aumento(num=0, aumento=0, formato=False):
    r = num + ((num * aumento) / 100)
    return r if formato == False else dados.moeda(r)

def desconto(num=0, desconto=0, formato=False):
    r = num - ((num * desconto) / 100)
    return r if formato == False else dados.moeda(r)

def dobro(num=0, formato=False):
    r = num * 2
    return r if formato == False else dados.moeda(r)

def metade(num=0, formato=False):
    r = num / 2
    return r if formato == False else dados.moeda(r)
