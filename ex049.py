print('Central da Tabuada')
n = int(input('Digite o numero que deseja ver a tabuada: '))
print('=-'*10)
print('TABUADA DO {}'.format(n))
for c in range(1, 11):
    print('{} X {} = {} '.format(n, c, c*n))
print('=-'*10)
