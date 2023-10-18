from datetime import date
print('==================================')
print(' COFEDERAÇÃO NACIONAL DE NATAÇÃO ')
print('==================================')
atual = date.today().year
nas = int(input('Ano de nascimento: '))
idade = int(atual - nas)
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: MASTER')
else:
    print('Classificação: MASTER')
