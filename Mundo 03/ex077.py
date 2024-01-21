palavras = ('kit', 'Copo', 'Taça', 'Mercadinho', 'Ideal', 'Ventilador', 'Sigilo', 'Perigoso')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
