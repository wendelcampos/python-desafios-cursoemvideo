def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mErro: Por favor, digite um numero inteiro valido\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31mUsuario preferiu não digitar esse numero!\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mErro: Por favor, digite um numero real valido\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31mUsuario preferiu não digitar esse numero!\033[m')
            return 0
        else:
            return n


i = leiaInt('Digite um numero inteiro: ')
f = leiaFloat('Digite um numero inteiro: ')
print(f'Voce digitou o numero inteiro {i} e o numero real {f}')
