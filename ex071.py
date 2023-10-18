print('='*30)
print(f'{"ANNYBANK":^30}')
print('='*30)
valor = int(input('Que valor deseja sacar? R$ '))
total = valor
while total != 0:
    n50 = int(valor / 50)
    total = total - (n50 * 50)
    n20 = int(total / 20)
    total = total - (n20 * 20)
    n10 = int(total / 10)
    total = total - (n10 * 10)
    n1 = int(total)
    total = total-total
if n50 != 0:
    print(f'Total de {n50} cédulas de R$ 50,00')
if n20 != 0:
    print(f'Total de {n20} cédulas de R$ 20,00')
if n10:
    print(f'Total de {n10} cédulas de R$ 10,00')
if n1 != 0:
    print(f'Total de {n1} cédulas de R$ 1,00')
