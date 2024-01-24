def notas(*n, sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit == True:
        if r['média'] >= 7:
            r['situação'] = 'Aprovado'
        elif 5 <= r['média'] <= 6:
            r['situação'] = 'Recuperação'
        else:
            r['situação'] = 'Reprovado'
    return r
print(notas(9, 2, 2, 5, sit=True))