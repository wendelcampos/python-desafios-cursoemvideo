from uteis import *
from arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    linha()
    print('MENU PRINCIPAL'.center(40))
    linha()
    print('\033[0;33m1 -\033[m ' '\033[0;34mVer pessoas cadastradas\033[m')
    print('\033[0;33m2 -\033[m ' '\033[0;34mCadastrar novas pessoas\033[m')
    print('\033[0;33m3 -\033[m ' '\033[0;34mSair do sistema\033[m')
    linha()
    try:
        n = int(input('\033[0;33mSua opção:\033[m '))
        sleep(0.2)
        if n == 1:
            linha()
            print('PESSOAS CADASTRADAS'.center(40))
            linha()
            lerArquivo(arq)
        elif n == 2:
            linha()
            print('NOVO CADASTRO'.center(40))
            linha()
            nome = str(input('Nome: ')).strip()
            while True:
                try:
                    idade = int(input('Idade: '))
                    cadastro(arq, nome, idade)
                    break
                except ValueError:
                    print(f'\033[0;31mErro! por favor, digite um numero inteiro valido\033[m')
        elif n == 3:
            break
        else:
            print(f'\033[0;31mErro! por favor digite um numero inteiro valido\033[m')
    except (NameError, ValueError):
        print(f'\033[0;31mErro! Digite um opção valida\033[m')

linha()
print('Saindo do Sistema... Ate logo!'.center(40))
linha()
