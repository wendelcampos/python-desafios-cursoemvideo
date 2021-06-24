y = ()
pares = ()
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        pares += (n,)
    y = y + (n,)

pares = ' '.join(str(pares) for pares in pares)

print(f'Voce digitou os valores: {y}')
print(f'O valor 9 apareceu {y.count(9)} vezes.')
if 3 in y:
    print(f'O valor 3 apareceu na {y.index(3) + 1}º posição.')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram: {pares}')
