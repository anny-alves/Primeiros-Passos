s = 0
cont = 0
for c in range(1, 501,2):
    if c%3 == 0:
        cont = cont +1
        s += c
print('A soma de todos dos {} entre 0 e 500 é igual a {}'.format(cont, s))
