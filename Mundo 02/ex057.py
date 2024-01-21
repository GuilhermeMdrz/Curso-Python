sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Informe seu sexo: [M/F] ')).strip().upper()[0]
print('O sexo {} foi registrado.'.format(sexo))
print('FIM')
