print('Gerador de PA')
print('-=-' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
while cont <= 10:
    print('{}-> '.format(primeiro), end='')
    primeiro += razao
    cont += 1
print('ACABOU !!')