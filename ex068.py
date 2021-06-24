from random import randint

print('-=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=-' * 20)
total = 0
while True:
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    if escolha == 'P':
        computador = randint(0, 10)
        if (jogador + computador) % 2 == 0:
            print('-=-' * 20)
            print(f'Voce jogou {jogador} e o computador {computador}. Total de {jogador + computador} é PAR')
            print('-=-' * 20)
            print('Voce VENCEU!')
            print('Vamos jogar novamente')
            total += 1
        if (jogador + computador) % 2 != 0:
            print('-=-' * 20)
            print(f'Voce jogou {jogador} e o computador {computador}. Total de {jogador + computador} é IMPAR')
            print('-=-' * 20)
            print('Voce PERDEU!')
            break
    if escolha == 'I':
        computador = randint(0, 10)
        if (jogador + computador) % 2 != 0:
            print('-=-' * 20)
            print(f'Voce jogou {jogador} e o computador {computador}. Total de {jogador + computador} é IMPAR')
            print('-=-' * 20)
            print('Voce VENCEU!')
            total += 1
        if (jogador + computador) % 2 == 0:
            print('-=-' * 20)
            print(f'Voce jogou {jogador} e o computador {computador}. Total de {jogador + computador} é PAR')
            print('-=-' * 20)
            print('Voce PERDEU!')
            break
print('-=-' * 20)
print(f'GAME OVER! Voce venceu {total} vezes')


