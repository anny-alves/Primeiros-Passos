from random import sample
from time import sleep
cont = int(0)
jogadas = dict()
for c in range(1, 5):
    jogadas[f'Jogador{c}'] = sample((1, 6), 1)
for k, v in jogadas.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
for i in sorted(jogadas, key = jogadas.get, reverse=True):
    cont += 1
    print(f'{cont}° Lugar: {i} com {jogadas[i]}')
    sleep(1)
