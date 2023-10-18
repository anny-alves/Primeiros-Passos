dados = (int(input('Digite um número: ')),
int(input('Digite outro número: ')),
 int(input('Digite mais um número: ')),
 int(input('Agora o último número: ')))
print(f' Você dicitou os valores {dados}')
print(f'O valor 9 apareceu {dados.count(9)}')
if 3 in dados:
    print(f'O valor 3 apareceu na {dados.index(3)+1}° posição')
else:
    print('o número 3 não consta nos valores digitados.')
print('Os valores pares foram ', end=' ')
for n in dados:
    if n % 2 == 0:
        print(f' {n}', end=' ')
