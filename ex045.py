from random import randint
from time import sleep
jogador = str(input('Digite entre pedra, papel e tesoura: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
computador = randint(1, 3)
escolha = ''
if computador == 1:
    escolha = 'papel'
elif computador == 2:
    escolha = 'tesoura'
elif computador == 3:
    escolha = 'pedra'

if jogador == 'pedra' and escolha == 'papel':
    print('O computador escolheu: {}'.format(escolha))
    print('Computador ganhou !!!!')
elif jogador == 'papel' and escolha == 'pedra':
    print('O computador escolheu: {}'.format(escolha))
    print('Jogador ganhou !!!')
elif jogador == 'tesoura' and escolha == 'papel':
    print('O computador escolheu: {}'.format(escolha))
    print('Jogador ganhou !!!!')
elif jogador == 'papel' and escolha == 'tesoura':
    print('O computador escolheu: {}'.format(escolha))
    print('Computador ganhou !!!!')
elif jogador == 'tesoura' and escolha == 'pedra':
    print('O computador escolheu: {}'.format(escolha))
    print('Computador ganhou !!!!')
elif jogador == 'pedra' and escolha == 'tesoura':
    print('O computador escolheu: {}'.format(escolha))
    print('Jogador ganhou !!!!')






