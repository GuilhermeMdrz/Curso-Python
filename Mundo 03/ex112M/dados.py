def leiadinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isnumeric:
            válido = True
            return float(entrada)
        if entrada.isalpha:
                print(f'ERRO: \"{entrada}\" é um preço inválido!')