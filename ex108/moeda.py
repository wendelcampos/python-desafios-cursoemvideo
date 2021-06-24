def metade(n=0):
    return n / 2


def dobro(n=0):
    return n * 2


def aumentando(n=0):
    return n + ((n * 10) / 100)


def diminuindo(n=0):
    return n - ((n * 13) / 100)


def moeda(n=0):
    return f'R${n:.2f}'.replace('.', ',')
