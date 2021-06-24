from time import sleep
n1 = int(input('Digite primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
opcao = 0
while opcao != 5:
    opcao = int(input('''OPERAÇÕES
        [1] SOMAR
        [2] MULTIPLICAÇÃO
        [3] MAIOR
        [4] NOVOS NUMEROS
        [5] SAIR DO PROGRAMA
        ESCOLHA A OPÇÃO: '''))
    if opcao == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('o {} é maior'.format(n1))
        elif n1 < n2:
            print('O {} é maior'.format(n2))
        else:
            print('O {} e {} são iguais'.format(n1, n2))
    elif opcao == 4:
        print('Informe os numeros novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print()
        print('Finalizando !!!!')
        sleep(1)
    else:
        print('Opção invalida. Tente novamente !!!')
    sleep(2)

print()
print('Fim do programa! Volte sempre !!')
print('===== FIM =====')
