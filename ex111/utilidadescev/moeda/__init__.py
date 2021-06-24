def metade(n):
    return n / 2


def dobro(n):
    return n * 2


def aumentando(n, porcentagem):
    return n + ((n * porcentagem) / 100)


def diminuindo(n, porcentagem):
    return n - ((n * porcentagem) / 100)


def linha():
    print('-' * 30)


def resumo(p=0, aumento=10, reducao=5):
    linha()
    print('RESUMO DO VALOR'.center(30))
    linha()
    print(f'Preço analisado: \tR${p:.2f}'.replace('.', ','))
    print(f'Dobro do preço:  \tR${dobro(p):.2f}'.replace('.', ','))
    print(f'Metade do preço: \tR${metade(p):.2f}'.replace('.', ','))
    print(f'{aumento}% de aumento:  \tR${aumentando(p, aumento):.2f}'.replace('.', ','))
    print(f'{reducao}% de redução:  \tR${diminuindo(p, reducao):.2f}'.replace('.', ','))
    linha()
