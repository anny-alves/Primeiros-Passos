matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l}. {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:^5}', end='')
        if matriz[l][c] %  2 == 0:
            spar += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares foi {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna foi {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[l][c]
    elif matriz[l][c]> mai:
        mai = matriz[l][c]
print(f'O Maior valor da segunda linha foi {mai}')
