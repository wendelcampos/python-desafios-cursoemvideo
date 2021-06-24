print('-=' * 50)
print('{:^90}'.format('BRASILEIRÃO 2021'))
print('-=' * 50)
times = ('America', 'Atletico Paranaense', 'Atlético', 'Atlético', 'Bahia',
         'Ceará', 'Chapecoense', 'Corinthians', 'Cuiabá', 'Flamengo',
         'Fluminense', 'Fortaleza', 'Grêmio', ' Internacional', 'Juventude',
         'Palmeiras', 'Red Bull Bragantino', 'Santos', 'São Paulo', 'Sport')

for t in times:
    print(t, end=', ')
print()
print('-=' * 50)
print(f'Os cincos primeiros são {times[0:5]}')
print('-=' * 50)
print(f'Os 4 ultimos sao {times[-4:]}')
print('-=' * 50)
print(f'Times em ordem alfabetica {sorted(times)}')
print('-=' * 50)
print(f'O Chapecoense esta em {times.index("Chapecoense") + 1}º posição')
