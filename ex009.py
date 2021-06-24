n1 = int(input('Digite o numero a ser multiplicado: '))
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = []

for x in range(len(lista)):
    resultado.append(n1 * lista[x])
resultado = ' '.join(str(c) for c in resultado)

print('=================================================')
print('a multiplicação de {} é: {}'.format(n1, resultado))


