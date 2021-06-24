def linha():
    print('-' * 30)


def area(l, c):
    print(f'A area de um terreno {l}x{c} é de {l * c}m.')


print('{:^30}'.format('Controle de Terrenos'))
linha()
largura = float(input('LARGURA (m): '))
comprimento = float(input("COMPRIMENTO (m): "))
area(largura, comprimento)
