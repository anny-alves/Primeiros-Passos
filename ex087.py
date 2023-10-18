matriz = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
somapar = soma3 = 0
maior2 = 0
for pos, c in enumerate(matriz):
    n = (int(input(f'Digite um valor para a posição {c}: ')))
    matriz[pos].append(n)
    if n % 2 == 0:
        somapar += n
    if pos == 2 or pos == 5 or pos == 8:
        soma3 += n
    if pos == 3 or pos == 4 or pos == 5:
        if pos == 3:
            maior2 = n
        else:
            if n > maior2:
                maior2 = n
print('-+-'*15)
print(f'[{matriz[0][2]}] [{matriz[1][2]}] [{matriz[2][2]}]')
print(f'[{matriz[3][2]}] [{matriz[4][2]}] [{matriz[5][2]}]')
print(f'[{matriz[6][2]}] [{matriz[7][2]}] [{matriz[8][2]}]')
print('-+-'*15)
print(f'A soma dos valores pares foi {somapar}')
print(f'A soma dos valores da terceira coluna foi {soma3}')
print(f'O Maior valor da segunda linha foi {maior2}')