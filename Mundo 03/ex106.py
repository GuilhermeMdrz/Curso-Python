c = ('\033[m', '\033[0;30;41m', '\033[0;30;43m', '\033[0;30;44m')
def mensagem(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0])
def ajuda(msg):
    print(help(msg))
while True:
    mensagem('SISTEMA DE AJUDA PyHELP', 2)
    resp = input('Função ou Biblioteca> ')
    if resp in 'FIMfim':
        break
    else:
        mensagem(f'ACESSANDO O MANUAL {resp}', 3)
        ajuda(resp)
mensagem('ATÉ LOGO', 1)
