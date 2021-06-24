lista = []
copia = []
while True:
    copia.append(str(input('Nome: ')))
    copia.append(float(input('NOTA 1: ')))
    copia.append(float(input('NOTA 2: ')))
    lista.append(copia[:])
    copia.clear()
    resp = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if resp not in 'S':
        break
print('-=' * 30)
print('Nº', end='')
print('{:>8}'.format('NOME'), end=' ')
print('{:>14}'.format('MEDIA'))
print('-' * 30)
for i, v in enumerate(lista):
    print(f'{i:<5}', end=' ')
    print(f'{v[0]:<6}', end=' ')
    print(f'{(v[1] + v[2]) / 2:>10}', end=' ')
    print()
print('-' * 30)
while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        print('FINALIZANDO....')
        break
    if aluno < len(lista):
        print(f'As notas de {lista[aluno][0]} foram {lista[aluno][1:]}')
    else:
        print('Opção invalida. Por favor tente novamente !')
print('<<< VOLTE SEMPRE !!!! >>>')




