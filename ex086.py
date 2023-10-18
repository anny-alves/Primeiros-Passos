matriz = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
for pos, c in enumerate(matriz):
    matriz[pos].append(int(input(f'Digite um valor para a posição {c}: ')))
print(f'[{matriz[0][2]}] [{matriz[1][2]}] [{matriz[2][2]}]')
print(f'[{matriz[3][2]}] [{matriz[4][2]}] [{matriz[5][2]}]')
print(f'[{matriz[6][2]}] [{matriz[7][2]}] [{matriz[8][2]}]')
#solução do professor
matriz = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}'))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}', end='')
    print()