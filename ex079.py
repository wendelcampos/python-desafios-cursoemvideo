lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado ! Não vou adicionar')
    opcao = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if opcao not in 'S':
        break
lista.sort()
print(f'Voce digitou os valores {lista}')
