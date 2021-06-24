p = float(input('Qual o seu peso ? (KG) '))
altura = float(input('Qual a sua altura ? (M) '))

imc = p / (altura ** 2)

print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta ABAIXO do peso')
elif 18.5 <= imc <= 25:
    print('Voce esta no Peso Ideal')
elif 25 <= imc <= 30:
    print('Voce esta no Sobrepeso')
elif 30 <= imc <= 40:
    print('Voce esta em Obsidade')
elif imc > 40:
    print('Voce esta em Obsidade morbida CUIDADO !!!')


