import math

cateto_oposto = float(input('Cateto Oposto: '))
cateto_adjacente = float(input('Cateto Adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
# hipotenusa = sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)
print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))