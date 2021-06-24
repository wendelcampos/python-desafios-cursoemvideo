jogador = {}
jogador['nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
c = 0
while c < partidas:
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
    c += 1
jogador['gols'] = gols

soma = 0
for g in gols:
    soma += g
jogador['total'] = soma
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for i, v in enumerate(gols):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
