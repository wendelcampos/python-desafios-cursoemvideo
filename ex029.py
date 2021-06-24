v = float(input('Velocidade do carro: '))
m = 0
if v > 80:
    print('MULTADO! Voce excedeu o limite permitido que é de 80km/h')
    m = (v - 80) * 7.00
    print('Voce pagara uma multa no valor de R${:.2f}'.format(m))
print('Tenha um bom dia! Dirija com segurança !!')



