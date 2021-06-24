lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    opcao = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if opcao not in 'S':
        break

print('-=' * 40)
print(f'A lista completa é {lista}')
for count in lista:
    if count % 2 == 0:
        pares.append(count)
    else:
        impares.append(count)
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
