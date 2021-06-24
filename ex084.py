pessoas = []
copia = []
pesada = leve = 0
while True:
    copia.append(str(input('Nome: ')))
    copia.append(float(input('Peso: ')))
    resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    pessoas.append(copia[:])
    copia.clear()
    if resp not in 'S':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas')
for p in pessoas:
    if p == 1:
        pesada = leve = p[1]
    else:
        if p[1] > pesada:
            pesada = p[1]
        if p[1] < pesada:
            leve = p[1]
print(f'O maior peso foi de {pesada}KG. Peso de', end=' ')
for v in pessoas:
    if v[1] == pesada:
        print(f'{v[0]}', end='... ')
print()
print(f'O menor peso foi de {leve}KG. Peso de', end=' ')
for x in pessoas:
    if x[1] == leve:
        print(f'{x[0]}', end='... ')

