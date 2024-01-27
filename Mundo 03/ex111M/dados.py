def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')

def resumo(num=0, taxaa=10, taxad=10):
    from ex111M import moeda, dados
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço analisado:":20} {dados.moeda(num)}')
    print(f'{"Dobro do preço:":20} {moeda.dobro(num, True)}')
    print(f'{"Metade do preço:":20} {moeda.metade(num, True)}')
    print(f'{"Ápos aumento:":20} {moeda.aumento(num, taxaa, True)}')
    print(f'{"Ápos desconto:":20} {moeda.desconto(num, taxad, True)}')
    print('-' * 30)
