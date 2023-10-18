listagem = ('Lápis', 1.5,
            'Borracha', 1,
            'Caderno', 25,
            'Estojo', 7.55,
            'transferidor', 6,
            'Compasso', 15,
            'Mochila', 105,
            'Canetas', 30,
            'livro', 56.30)
print('-'*30)
print(f'{"Lista de Preços":^30}')
print('-'*30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<23}', end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')
