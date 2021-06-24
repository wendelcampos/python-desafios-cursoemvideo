soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        cont += 1
        soma += n
print('Voce informou {} numeros PARES e a soma é {}'.format(cont, soma))
