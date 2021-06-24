def metade(n, fomart=False):
    if fomart:
        return f'R${n / 2:.2f}'
    else:
        return n / 2


def dobro(n, format=False):
    if format:
        return f'R${n * 2:.2f}'
    else:
        return n * 2


def aumentando(n, porcentagem=0, format=False):
    if format:
        return f'R${n + ((n * porcentagem) / 100):.2f}'
    else:
        return n + ((n * 10) / 100)


def diminuindo(n, reducao=0, format=False):
    if format:
        return f'R${n - ((n * reducao) / 100):.2f}'
    else:
        return n - ((n * reducao) / 100)
