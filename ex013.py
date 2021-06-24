salario = float(input('Digite o salario: '))
porcentagem = float(input('Digite a porcentagem: '))
porcentagem = (salario * porcentagem) / 100
print('O novo salario é de {:.2f}'.format(salario + porcentagem))