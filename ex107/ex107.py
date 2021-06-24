from moeda import metade, dobro, aumentando, diminuindo

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p:.2f} é {metade(p)}')
print(f'O dobro de R${p:.2f} é {dobro(p)}')
print(f'Aumentando 10% de R${p:.2f} é {aumentando(p)}')
print(f'Dimunuindo 13% de R${p:.2f} é {diminuindo(p)}')
