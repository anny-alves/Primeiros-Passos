#contagem de 1 a 50 mostrando apenas pares#
#modo1#
for c in range(2,51,2):
    print(c, end=' ')
print('fim')
#modo2#
for c in range(1,51):
    if c%2 == 0:
        print(c, end=' ')
print('Fim')
