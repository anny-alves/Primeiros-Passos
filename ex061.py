#progressão aritimétrica
print("="*30)
print('{:^25}'.format('10 TERMOS DE UMA PA'))
print("="*30)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
termo = t
while c <= 10:
    print('{}'.format(termo), end=' ')
    termo += r
    c += 1
