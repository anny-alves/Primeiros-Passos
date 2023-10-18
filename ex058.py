import random
print('====== Adivinhe o número =====')
n = int(random.randint(1, 10))
na = 0
c = 0
print('Olá sou seeu computador, pensei em um número entre 1 e 10.\n Tente adivinhar!!!')
na = 0
while n != na:
    na= int(input('Adivinhe o número: '))
    c += 1
    if na> n:
        na = int(input('Menor... Tente adivinhar: '))
    elif na < n:
        na = int(input('Maior... Tente adivinhar: '))
    elif na == n:
        print('VOCÊ ACERTOU!!!\n Você precisou de {} tentativas para isso!'.format(c))
