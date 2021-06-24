from random import randint
from time import sleep
while True:
    ia = randint(0, 5)
    print('-=-' * 20)
    print('Vou pensar em um numero entre 0 e 5. Tente adivinhar.....')
    print('-=-' * 20)
    n = int(input('Em que numero eu pensei ???? '))
    print('PROCESSANDO...')
    sleep(3)
    if n == ia:
        print('Parabens voce conseguiu me vencer !!!')
    else:
        print('Ganhei !!!! eu pensei no {} e não no numero {} !!!!'.format(ia, n))
