import random
print('====== Adivinhe o número =====')
na = random.randint(1,5)
n = int(input('Digite um número de 1 a 5: '))
if n == na:
    print("Prabéns, você ganhou!")
else:
    print('O número escolhido era {}. \n Você perdeu, tente novamente.'. format(na))
