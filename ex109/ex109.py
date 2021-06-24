import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p:.2f} é {moeda.metade(p, True)}')
print(f'O dobro de R${p:.2f} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% de R${p:.2f} é {moeda.aumentando(p, 10, True)}')
print(f'Dimunuindo 13% de R${p:.2f} é {moeda.diminuindo(p, 13, True)}')
