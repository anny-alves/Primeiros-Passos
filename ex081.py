r = ' '
lista = []
while r not in 'Nn':
    n = int(input('Digite um número: '))
    lista.append(n)
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
lista.sort(reverse=True)
print('-=-'*15)
print(f"Você digitou {len(lista)} valores"
      f"\nOs valores digitados em ordem decrescente foram {lista}")
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
