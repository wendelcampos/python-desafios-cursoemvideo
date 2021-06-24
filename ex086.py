matriz = [[], [], []]
for a in range(0, 3):
    linha1 = int(input(f'Digite um valor para [0, {a}]: '))
    matriz[0].append(linha1)
for b in range(0, 3):
    linha2 = int(input(f'Digite um valor para [1, {b}]: '))
    matriz[1].append(linha2)
for c in range(0, 3):
    linha3 = int(input(f'Digite um valor para [2, {c}]: '))
    matriz[2].append(linha3)


print('-=-' * 20)

for i, v in enumerate(matriz):
    for c in v:
        print(f'[{c:^5}]', end=' ')
    print()

