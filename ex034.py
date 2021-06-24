salario = float(input('Qual o salario do funcionario R$ '))
if salario > 1250:
    porcentagem = (salario * 10) / 100
    print("O salario ira ficar com R$ {:.2f}".format(salario + porcentagem))
else:
    porcentagem = (salario * 15) / 100
    print("O salario ira ficar com R$ {:.2f}".format(salario + porcentagem))

