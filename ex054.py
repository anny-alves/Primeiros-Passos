#grupo da maior idade#
from datetime import date
atual = date.today().year
tmaior = 0
tmenor = 0
for c in range(1, 8):
    nasc = int(input('Em que no essa pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        tmaior += 1
    else:
        tmenor += 1
print('Esse grupo tem {} pessoas de maior e {} pessoas de menor'.format(tmaior, tmenor))
