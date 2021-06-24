s = 0
total = 0
while True:
    n = int(input('Digite um numero (999 para parar): '))
    if n == 999:
        break
    s += 1
    total += n
print(f'A soma dos {s} valores foi {total} !')
