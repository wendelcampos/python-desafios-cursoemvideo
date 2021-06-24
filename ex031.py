v = float(input('Distância da viagem em KM: '))
p = 0
if v <= 200:
    p = v * 0.50
    print('Voce pagará o valor de R${:.2f} para viagem até 200km'.format(p))
else:
    p = v * 0.45
    print('Voce pagará o valor de R${:.2f} para viagem acima de 200Km'.format(p))
