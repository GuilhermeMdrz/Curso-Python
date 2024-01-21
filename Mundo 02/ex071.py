valor = int(input('Quanto você quer sacar? R$'))
total = valor
cédula = 50
totalc = 0
while True:
    if total >= cédula:
        total -= cédula
        totalc += 1
    else:
        if totalc > 0:
            print(f'Você receberá {totalc} de R${cédula}')
        if cédula == 50:
            cédula = 20
        if cédula == 20:
            cédula = 10
        if cédula == 10:
            cédula = 1
        totalc = 0
        if total == 0:
            break
