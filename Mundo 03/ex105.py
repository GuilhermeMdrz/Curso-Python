def notas(*n, sit=False):
    """
    -> Analisa as notas de um aluno e mostra algumas informações.
    :panam n: Notas a serem analisadas.
    :panam sit: (Opcional) Mostra a situação de acordo com a média.
    :return: Retorna os dados após serem analisados.
    """
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
