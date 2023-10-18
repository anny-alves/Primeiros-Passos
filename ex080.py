lista = list()
for c in range(0,5):
    valor = int(input('Digite um valor: '))
    if c == 0:
        lista.append(valor)
        print(f'Adcionado ao final da lista...')
    elif c == 1:
        if valor >= lista[0]:
            lista.insert(c, valor)
            print(f'Adcionado ao final da lista...')
        else:
            lista.insert(0, valor)
            print(f'Adcionado na  posição {c} da lista...')
    elif c == 2:
        if valor >= lista[1]:
            lista.insert(c, valor)
            print(f'Adcionado ao final da lista...')
        elif valor >= lista[0]:
            lista.append(1, valor)
            print(f'Adcionado na posição 1 da lista...')
        else:
            lista.append(0, valor)
            print('Adicionado no inicio da lista...')

