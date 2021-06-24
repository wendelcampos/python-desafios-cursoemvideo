preco = float(input('Digite o preco do produto R$ '))
porcentagem = float(input('Digite a porcentagem: '))
porcentagem = (preco * porcentagem) / 100
print('O seu novo preço com desconto é R${:.2f}'.format(preco - porcentagem))