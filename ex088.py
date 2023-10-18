import random
print('-'*30)
print(f'{"MEGA SENA":^30}')
print('-'*30)
njogos = int(input('Quantos jogos você quer gerar? '))
jogos = list()
jind = list()
for c in range(0,njogos):
    jind = sorted(random.sample(range(60),6))
    jogos.append(jind[:])
    jind.clear()
sorted(jogos)
for c in range(0, njogos):
    print(f'Jogo {c+1}: {jogos[c]}')
