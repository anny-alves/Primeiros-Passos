# menu dos dois valores #
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo valor: '))
o = 0
while o != 5:
    print('===== MENU =====')
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior valor')
    print('[ 4 ] novos números')
    print('[ 5 ] Sair')
    o = int(input('Digite a opção desejada: '))
    if o == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif o == 2:
        print('{} * {} = {}'.format(n1, n2, n1*n2))
    elif o == 3:
        if n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
        elif n2> n1:
            print('{} é maior que {}.'.format(n2, n1))
        else:
            print('Os dois vlores são iguais.')
    elif o == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo valor: '))
    else:
        print('Opção inálida, tente novamente!')
print('Obrigado.')
