jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Partidas jogadas: '))
for c in range(0, partidas):
    gols.append(int(input(f'Gols da {c+1}° partida: ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-=-'*20)
print(jogador)
print('-=-'*15)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-=-'*20)
print(f'O jogador {jogador["nome"]} jogou {partidas}.')
for c, i in enumerate(gols):
    print(f'Na partida {c+1}, fez {i} gols.')
print(f'Foi um total de {sum(gols)}')
