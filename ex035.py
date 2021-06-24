print('-=' * 20)
print('Analisador de Triangulos')
print('-=' * 20)
r1 = float(input('Medida da primeira reta: '))
r2 = float(input('Medida da segunda reta: '))
r3 = float(input('Medida da terceira reta: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r3 + r2) > r1:
    print('As retas podem formar um triangulo !!! ')
else:
    print('As retas não podem formar um triangulo !!')
