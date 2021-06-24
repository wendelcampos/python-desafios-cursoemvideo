print('{:=^40}'.format(' LOJAS WENDEL '))
produto = float(input('Preço das compras R$ '))
pagamento = str(input('''FORMAS DE PAGAMENTO
[1] á vista 
[2] á vista no cartão 
[3] em ate 2x no cartão 
[4] parcelado no cartão: 
Qual é a opção: '''))

if pagamento == '1':
    print('O valor do produto a ser pago é de: R${:.2f}'.format(produto - (produto * 10) / 100))
elif pagamento == '2':
    print('O valor do produto a ser pago é de: R${:.2f}'.format(produto - ((produto * 5) / 100)))
elif pagamento == '3':
    print('O valor do produto a ser pago é de: 2x parcelas de R${:.2f}'.format(produto / 2))
elif pagamento == '4':
    parcelas = int(input('Digite o numero de parcelas: '))
    parcelamento = (produto + (produto * 20) / 100) / parcelas
    if parcelas >= 3:
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(produto, produto + (produto * 20) / 100))
        print('O valor do produto a ser pago é de: {}x parcelas de R${:.2f}'.format(parcelas, parcelamento))
else:
    print('Opção invalida de pagamento. Tente novamente')