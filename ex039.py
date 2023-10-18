from datetime import date
atual = date.today().year
print(' Verificação de situação de alistamento militar')
nome = str(input('Insira seu nome: '))
sexo = str(input('Escolha o seu sexo F/M: ')).upper()
if sexo == 'F':
    print("O alistamento militar não é obrigatório pra você")
else:
    an = int(input('Insira o ano em que você nasceu: '))
    idade = atual - an
    if idade == 18:
        print('{}, você precisa se alistar esse ano!'.format(nome))
    elif idade < 18:
        print('{}, faltam {} anos para você se alistar, isso ocorrerá em {}'.format(nome, 18-idade, an+18))
    else:
        print('{}, você perdeu seu praso. Você deveria ter se alistado a {} anos, no ano de {}'.format(nome, idade-18, an+18))
