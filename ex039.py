from datetime import date

atual = date.today().year

nasc = int(input('Digite o seu ano de nascimento: '))

idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE !!!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para o seu alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {} ano'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print("Voce já deveria ter se alistado a {} anos".format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {} ano'.format(ano))
