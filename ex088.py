from random import randint
from time import sleep
print('-=-' * 30)
print('{:^80}'.format('SORTEIO DA MEGASENA'))
print('-=-' * 30)
sorteio = int(input('Quantos jogos voce quer que eu sorteie: '))
print(F'-=-=-=-= SORTEANDO {sorteio} JOGOS -=-=-=-')
c = 0
while c < sorteio:
    lista = []
    for n in range(0, 6):
        lista.insert(0, randint(1, 60))
        sleep(0.2)
    c += 1
    lista.sort()
    print(f'Jogo {c}: {lista}')

print()
print(F'-=-=-=-= BOA SORTE -=-=-=-')


