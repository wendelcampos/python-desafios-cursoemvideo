casa = float(input('Valor da casa: R$ '))
salario = float(input('Valor do salario: R$ '))
qtd_anos = int(input('Quantos anos ira pagar: '))

prestacao = casa / (qtd_anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, qtd_anos, prestacao))

salario_porcentagem = (salario * 30) / 100
if prestacao <= salario_porcentagem:
    print('Emprestimo CONCEDIDO')
else:
    print('Emprestimo NEGADO')


