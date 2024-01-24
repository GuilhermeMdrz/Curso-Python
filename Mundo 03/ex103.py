def ficha(nome='<desconhecico>', gols=0): 
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'
n = str(input('Nome do jogador: '))
g = str(input('Total de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else: 
    ficha(n, g)
print(ficha(n, g))
