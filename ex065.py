opcao = 'S'
cont = soma = maior = menor = 0
while opcao != 'N':
    n = int(input('digite um numero: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opcao = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
print('Voce digitou {} numeros e a media foi {:.2f}'.format(cont, (soma / cont)))
print('O maior valor foi de {} e o menor foi de {}'.format(maior, menor))
