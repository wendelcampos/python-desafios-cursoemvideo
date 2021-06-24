l1 = float(input('Digite o primeiro segmento: '))
l2 = float(input('Digite o segundo segmento: '))
l3 = float(input('Digite o terceiro segmento: '))

if (l1 + l2) > l3 and (l1 + l3) > l2 and (l3 + l2) > l1:
    if l1 == l2 == l3:
        print('Triangulo Equilatero')
    elif l1 != l2 != l3 != l1:
        print('Triangulo Escaleno')
    else:
        print('Triangulo Isosceles')
else:
    print('Não podem formar um triangulo')

