from datetime import date
data = date.today().year
nasc = int(input('Digite o ano de nascimento: '))

idade = data - nasc

print('Quem nasceu em {} tem {} anos'.format(nasc, idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade<= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')


