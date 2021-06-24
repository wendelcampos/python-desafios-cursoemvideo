maior = 0
homem = 0
mulher = 0
while True:
    print('=' * 40)
    print('CADASTRE UMA PESSOA')
    print('=' * 40)

    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F] ')).upper().strip()[0]
    print('=' * 40)

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        mulher += 1
    if opcao not in 'S':
        break

print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos?: {maior}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')
