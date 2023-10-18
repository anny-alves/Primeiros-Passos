lista = []
listapar = []
listaimpar = []
r = ' '
while r not in 'Nn':
    lista.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
for pos in range(len(lista)):
    if lista[pos] % 2 == 0:
        listapar.append(lista[pos])
    else:
        listaimpar.append(lista[pos])
print(f'A lista completa é \n{lista}')
print(f'A lista de números pares é \n{listapar}')
print(f'A lista de números impares é \n{listaimpar}')
