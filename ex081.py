lista = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    opcao = str(input('Quer continuar [S/N] ')).upper().strip()[0]
    if opcao not in 'S':
        break

print(f'Voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')