from time import (sleep)


def linha():
    print('-=-' * 20)


def contador(i, f, p):
    if p == 0:
        p = 1
    if i < f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for c in range(i, f+1, p):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
    if i > f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for c in range(i, f-1, -p):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')


linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = abs(int(input('Passo: ')))
linha()
contador(inicio, fim, passo)
