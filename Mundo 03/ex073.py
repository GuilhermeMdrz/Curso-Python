times = ('EC Vitória', 'Juventude', 'Criciúma', 'Atlético-GO', 'Novorizontino', 'Mirassol', 'Sport Recife',
         'Vila Nova', 'CRB', 'Guarani', 'Ceará SC', 'Botafogo SP', 'Avaí', 'Ituano', 'Ponte Preta', 'Chapecoense',
         'Sampaio Corrêa', 'Tombense', 'Londrina', 'ABC')
print(f'Os times que integram a séria B do Brasileirão 2023 são {times}.')
print(f'Os cinco primeros colocados são {times[:5]}.')
print(f'Os quatro últimos colocados são {times[16:]}.')
print(f'Os times em ordem alfabética: {sorted(times)}.')
print(f'O time da Chapecoense está na posição {times.index("Chapecoense") + 1}.')
