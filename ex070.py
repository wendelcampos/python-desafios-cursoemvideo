print('='*40)
print('LOJA SUPER BARATÃO')
print('='*40)

opcao = 'S'
soma = 0
caro = 0
cont = 0
produto_barato = ' '
menor = 0
while opcao != 'N':
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    opcao = ' '
    while opcao not in 'NS':
     opcao = str(input('Quer continuar? [N/S] ')).upper().strip()[0]
    soma += preco
    if cont == 1:
        menor = preco
        produto_barato = produto
    else:
        if preco < menor:
            menor = preco
            produto_barato = produto
    if opcao not in 'S':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R$ {soma:.2f}')
print(f'Temos {caro} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {produto_barato} que custa R${menor:.2f}')