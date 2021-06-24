n = int(input('Digite um numero: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end= '')
    print('{} '.format(c), end=' ')
print()
print('\n\033[mO numero {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print()
    print('E por isso que ele É PRIMO!!')
else:
    print()
    print('E por isso que ele NÂO É PRIMO !!')

