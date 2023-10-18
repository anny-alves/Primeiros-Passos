lista = list()
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(lista)
print(f'O maior valor foi {max(lista)} e estava na posição ', end=' ')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')
print()
print(f'O mnor valor foi {min(lista)} e estava na posição ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')
print('Fim')
