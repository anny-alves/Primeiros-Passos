from random import randint
num = (randint(0, 100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
print(f'Os números sorteados foram', end=' ')
for c in range(0,5):
    print(f'{num[c]}', end=' ')
print(f'\nO maior valor sortedo foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')