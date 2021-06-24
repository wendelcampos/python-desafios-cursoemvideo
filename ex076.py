listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90)
print('-='*30)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-='*30)
for x in range(0, len(listagem)):
    if x % 2 == 0:
        print(f'{listagem[x]:.<30}', end='')
    else:
        print(f'R$ {listagem[x]:>5.2f}')