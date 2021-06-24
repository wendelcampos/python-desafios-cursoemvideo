sexo = str(input('SEXO [M] / [F]: ')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    print('Dados invalidos.')
    sexo = str(input('Por favor, informe seu sexo: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

