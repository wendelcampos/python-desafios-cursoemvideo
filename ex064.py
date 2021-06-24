cont = 0
soma = 0
n = 0
n = int(input('Digite um numero: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um numero: '))
print('foram digitados {} numeros e a soma entre eles é {}'.format(cont, soma))



