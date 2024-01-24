def vota(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos, você NÃO VOTA!'
    elif 16<= idade < 18 or idade >= 65:
        return f'Com {idade} anos, o voto é OPCIONAL!'
    else: 
       return f'Com {idade} anos, o voto é  OBRIGATÓRIO!'
print('-' * 30)
nascimento = int(input('Em que ano você nasceu? '))
print(vota(nascimento))
