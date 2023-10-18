# analisador completo #
idades = 0
maior = 0
velho = 0
mulheres = 0
for c in range(1, 5):
    print( '----- {}° PESSOA -----'.format(c) )
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Sexo[F/M]: ')).upper()
    idades += i
    if s == 'M':
        if i >= maior:
             maior = i
             velho = n
    elif i < 20:
        mulheres += 1
media = idades / 4
print('A média das idades foi de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres))
