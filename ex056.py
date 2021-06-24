soma_idade = 0
mulher = 0
nome_maior = 0
homem_maior = 0
for c in range(1, 5):
    print('----- {} PESSOA -----'.format(c))
    nome = str(input('Nome? ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).lower().strip()
    soma_idade += idade
    if sexo == 'f' and idade < 20:
        mulher += 1
    if idade == 1 and sexo == 'm':
        nome_maior = nome
        homem_maior = idade
    else:
        if idade > homem_maior:
            nome_maior = nome
            homem_maior = idade

print()
print('A media de idade do grupo é de {} anos'.format(soma_idade / 4))
print('O homem mais velho tem {} anos e se chama {}.'.format(homem_maior, nome_maior))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher))
