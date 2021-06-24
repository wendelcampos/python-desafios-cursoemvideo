from random import randint
from time import sleep
computador = randint(0, 11)
jogador = int(input('Adivinhe o numero que estou pensando: '))
print('===== LOADING =====')
sleep(1)
tentativas = 0
acertou = False
while not acertou:
    if jogador == computador:
        acertou = True
    if jogador < computador:
        print('Mais...Tente mais uma vez.')
        jogador = int(input('Adivinhe o numero que estou pensando: '))
        tentativas += 1
        print('===== LOADING =====')
        sleep(1)
    if jogador > computador:
        print('Menos...Tente mais uma vez.')
        jogador = int(input('Adivinhe o numero que estou pensando: '))
        tentativas += 1
        print('===== LOADING =====')
        sleep(1)
print()
print('Jogador acertou com {} tentativas. Parabens !!!!!'.format(tentativas))
