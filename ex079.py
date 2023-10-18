op = 'S'
lista = list()
while op != 'N':
    valor = (int(input('Digite um número:')))
    if valor not in lista:
        lista.append(valor)
    else:
        print('Valor duplicado, não vou adicionar.')
    op = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
lista.sort()
print(f'Estes foram os números digitados: {lista}')

