def fatorial(n=0, show=False):
    '''
    -> Calcula o Fatorial de um numero:
    :param n: O numero a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: o valor do Fatorial de um numero n.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(f' x ', end=' ')
            else:
                print(f' = ', end=' ')
        f *= c
    return f


num = int(input('Digite o numero: '))
print(fatorial(num, show=True))
help(fatorial)