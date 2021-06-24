from datetime import date

pessoa = {}
pessoa['nome'] = str(input('Nome: '))
atual = date.today().year
ano_nascimento = int(input('Ano de Nascimento: '))
pessoa['idade'] = atual - ano_nascimento
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salario R$ '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratacao'] + 35) - date.today().year)
print('-=-' * 20)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')
