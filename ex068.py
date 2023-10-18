# Jogo do impar par
from random import randint
print('-='*30)
print('VAMOS JOGAR IMPAR OU PAR')
print('-='*30)
cont = 0
while True:
    comp = randint(0, 10)
    pessoa = int(input('Digite um númeto de 0 a 10: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    soma = comp + pessoa
    if escolha == 'I' and soma%2 != 0:
        cont += 1
        print(f'Voê jogou {pessoa} e o computador {comp}. Total de {soma} é IMPAR.\n VOCÊ VENCEU!')
        print('Vamos jogar novamente')
        print('=-'*30)
    elif escolha == 'P' and soma % 2 == 0:
        cont += 1
        print(f'Voê jogou {pessoa} e o computador {comp}. Total de {soma} é PAR.\n VOCÊ VENCEU!')
        print('Vamos jogar novamente')
        print('=-' * 30)
    elif escolha == 'I' and soma % 2 == 0:
        print(f'Voê jogou {pessoa} e o computador {comp}. Total de {soma} é PAR.\n VOCÊ PERDEU!')
        break
    elif escolha == 'P' and soma % 2 != 0:
        print(f'Voê jogou {pessoa} e o computador {comp}. Total de {soma} é IMPAR.\n VOCÊ PERDEU!')
        break
print(f'GAME OVER!!! Você venceu {cont} vezes')