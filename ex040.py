print(' ====== Escola da Anny ======')
nome = str(input('Insira seu nome: '))
n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))
med = (n1 + n2)/2
print('{}, sua média foi {}'.format(nome, med))
if med >= 7:
    print('Você está aprovado: ')
elif med >= 5 and med < 7:
    print('Você não foi aprovado. Com essa média, você tem direito a recuperação>')
else:
    print('Sua média foi abaixo de 5, com isso está reprovado sem direito a recuperação')
