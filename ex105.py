def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mais notas e situações de varios alunos.
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionario com varias informações sobre a situação da turma.
    '''
    notas = {}
    notas['total'] = len(n)
    notas['maior'] = max(n)
    notas['menor'] = min(n)
    notas['media'] = sum(n) / len(n)
    if sit:
        if notas['media'] >= 7:
            notas['situacao'] = 'BOA'
        elif notas['media'] >= 5:
            notas['situacao'] = 'RAZOAVEL'
        else:
            notas['media'] = 'RUIM'
    return notas


resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
# help(notas)
