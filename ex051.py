#progressão aritimétrica#
print("="*30)
print('{:^25}'.format('10 TERMOS DE UMA PA'))
print("="*30)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = t + (10-1) * r
for c in range(t, decimo+r, r):
    print('{}'.format(c), end=' -> ')
print('fim')
for c in range(0, 10):
    print(t, end=' -> ')
    t = t + r
print('Fim')