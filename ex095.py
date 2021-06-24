jogadores = []
jogador = {}
total = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    c = 0
    gols = []
    while c < partidas:
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
        c += 1
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    jogador.clear()
    while True:
        resp = str(input('Quer continuar [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if resp not in 'S':
        break

print('-=' * 20)
print('cod', '{:>6}'.format('nome'), '{:>10}'.format('gols'), '{:>12}'.format('total'))
# print('cod', end='')
# for c in jogadores[0]:
#     print(f'{c:>10}', end='')
# print()
print('-' * 40)
for k, v in enumerate(jogadores):
    print(f'{k:>2}', end='')
    for d in v.values():
        print(f'{str(d):>10}', end='')
    print()
print('-' * 40)
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if dados == 999:
        break
    if dados < (len(jogadores)):
        print('-- LEVANTAMENTO DO JOGADOR Padrão:')
        for i, v in enumerate(jogadores[dados]["gols"]):
            print(f'No jogo {i} fez {v} gols.')
    else:
        print(f'Erro! Não existe jogador com codigo {dados}! Tente novamente')
print('<< VOLTE SEMPRE >>')