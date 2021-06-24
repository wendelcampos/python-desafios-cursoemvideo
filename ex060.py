n = int(input('Digite um numero: '))
print('Calculando {}! ='.format(n), end=' ')
f = 1
while n > 0:
    print('{}'.format(n), end=' ')
    print('x' if n > 1 else '= ', end=' ')
    f *= n
    n -= 1
print('{}'.format(f))
