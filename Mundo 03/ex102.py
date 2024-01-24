def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado,
    :param show: {Opcional} Mostra ou não a conta.
    :return: O valor fatorial de um número num.
    """
    from math import factorial
    if show == True:
        f = 1
        c = num
        print('Calculando {}! = '.format(num), end='')
        while c > 0:
            print('{}'.format(c), end='')
            print(' x ' if c > 1 else ' = ', end='')
            f *= c
            c -= 1
        print(f)
    else:
        return f'{num}! = {factorial(num)}'
print('-=-' * 30)
print(fatorial(5, True))
help(fatorial)
