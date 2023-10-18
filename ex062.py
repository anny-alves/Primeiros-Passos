#progressão aritimétrica 2.0
print("="*30)
print('{:^25}'.format('10 TERMOS DE UMA PA'))
print("="*30)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
termo = t
total = 0
mais = 10
while mais !=0:
    total += mais
    while c <= total:
        print('{}'.format(termo), end=' ')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos mais você deseja ver? '))
print('FIM')