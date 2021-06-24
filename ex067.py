while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    print('=' * 50)
    if n < 0:
        break
    cont = 1
    while cont < 11:
        print(f'{n} x {cont} = {n * cont}')
        cont += 1
    print('=' * 50)

print('PROGRAMA TABUADA ENCERRADO.Volte Sempre !')
