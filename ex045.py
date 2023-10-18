from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('O computador escolheu {}'.format(itens [computador]))

print(' PEDRA PAPEL OU TESOURA')
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Escolha sua jogada: '))
print('JO')
print('KEN')
print('PO!!!')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Você escolheu {}'.format(itens [jogador]))
print('O computador escolheu {}'.format(itens [computador]))
if jogador == computador:
    print('Jogo EMPATADO!')
elif jogador == 0 and computador == 2:
    print('VOCÊ VENCEU!!!')
elif jogador == 1 and computador == 0:
    print('VOCÊ VENCEU!!!')
elif jogador == 2 and computador == 1:
    print('VOCÊ VENCEU!!!')
elif computador == 0 and jogador == 2:
    print('O COMPUTADOR VENVEU!')
elif computador == 2 and jogador == 1:
    print('O COMPUTADOR VENVEU!')
elif computador == 1 and jogador == 0:
    print('O COMPUTADOR VENVEU!')
else:
    print('Opção incorreta, tente novamente')
