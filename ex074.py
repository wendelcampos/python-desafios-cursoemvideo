from random import randint
n = ()
for c in range(0, 5):
    n += (randint(0, 6),)
n = ' '.join(str(c) for c in n)
print(f'Numeros selecionados pelo computador: {n}')
print(f'O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')

