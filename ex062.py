print('Gerador de PA')
print('-=-' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}-> '.format(primeiro), end='')
        primeiro += razao
        cont += 1
    print('PAUSA !!')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
