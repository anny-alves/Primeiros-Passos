# Média, maior e menor valor
resp = 'S'
cont = soma = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
media = soma / cont
print('A média dos números foi {} \n o maior e menor valor, respectivamente foram {} e {}'.format(media, maior, menor))
print('Fim!')
