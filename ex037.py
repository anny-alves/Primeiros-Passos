num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[ 1 ] Para Binário
[ 2 ] Para Octal
[ 3 ] Para Hexadecimal''')
t = int(input('Escolha sua opção: '))
if t == 1:
    print(' o número {} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif t == 2:
    print('O número {} convertido para Octal é igual a {}'.format(num. oct(num)[2:]))
elif t == 3:
    print('O número {} convertido para Hexadecimal é igual a {};'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.')