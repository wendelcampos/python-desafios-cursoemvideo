from time import sleep


def linha():
    print('-=-' * 20)


def maior(* num):
    pos = maior = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.4)
    while pos < len(num):
        if pos == 1:
            maior = num[pos]
        else:
            if num[pos] > maior:
                maior = num[pos]
        pos += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


linha()
maior(2, 9, 4, 5, 7, 1)
linha()
maior(4, 7, 0)
linha()
maior(1, 2)
linha()
maior(6)
linha()
maior()
linha()
