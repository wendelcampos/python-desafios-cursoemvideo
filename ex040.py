n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

print('Quem tirou {} e {} tem a media {}'.format(n1, n2, m))

if m <= 5.0:
    print('Reprovado')
elif m > 5.0 and m <= 6.9:
    print('Recuperação')
elif m >= 7.0:
    print('Aprovado')
