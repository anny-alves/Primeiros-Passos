print('-'*30)
print(f'{"LISTA DE COMPRAS":^30}')
print('-'*30)
total = umk = barato = cont = 0
menor = ' '
while True:
    item = str(input('Nome do Ítem: '))
    preço = float(input('Valor: R$'))
    cont += 1
    opc = ' '
    if preço >= 1000:
        umk +=1
    total += preço
    if cont == 1:
        barato = preço
        menor = item
    else:
        if preço < barato:
            barato = preço
            menor = item
    while opc not in 'SN':
        opc = str(input('Cadastrar mais um ítem? [S/N]: ')).strip().upper()[0]
    if opc == 'N':
            break
print(f''' O total da compra foi R${total}\n
{umk} itens da lista custam mais que R$ 1000,00\n
O produto mais barato foi {menor} custando {barato}''')
