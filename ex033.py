n1 = int(input('Digite primeiro numero: '))
n2 = int(input('Digite segundo numero: '))
n3 = int(input('Digite terceiro numero: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#################################
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print()
print('O maior valor dos numeros digitados é: {}'.format(maior))
print('O menor valor dos numeros digitados é: {}'.format(menor))
