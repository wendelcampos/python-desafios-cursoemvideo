from random import randint
from time import sleep


def sorteio(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lst.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.2)
    print('PRONTO!')


def somaPar(lst):
    soma = 0
    c = 0
    while c < len(lst):
        if lst[c] % 2 == 0:
            soma += lst[c]
        c += 1
    print(f'Somando os valores pares de {lst}, temos {soma}')


numeros = []
sorteio(numeros)
somaPar(numeros)
