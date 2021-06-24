pessoas = []
pessoa = {}
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).upper().strip()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    pessoa.clear()
    while True:
        resp = str(input('Deseja continuar [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if resp not in 'S':
        break
print('-=' * 20)
print(f' - O grupo tem {len(pessoas)} pessoas')
media = 0
for c in pessoas:
   media += (c['idade']) / len(pessoas)
print(f' - A média de idade é de {media:.2f} anos')
print(f' - As mulheres cadastradas foram:', end=' ')
for m in pessoas:
     if m['sexo'] == 'F':
        print(f'{m["nome"]}', end=' ')
print()
print(f' - Listas das pessoas que estao acima da média:')
for p in pessoas:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('<< ENCERRADO >>')

