num = [[], []]
for c in range(1,8):
    n = int(input(f'Digite o {c}° número: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print(f'Os números pares foram {sorted(num[0])} \nOs números ímpares foram {sorted(num[1])}')
