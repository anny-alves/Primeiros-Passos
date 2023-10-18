a = int(input(' Insira o primeiro valor: '))
b = int(input('Insira o segundo valor: '))
c = int(input('Insira o terceiro valor: '))
# Verificando o menor valor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o maior valor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor dig/itado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
