h = float(input('Digite a altura da parede em metros: '))
l = float(input('Digite a largura da parede em metros: '))
a = h * l
lit = a / 2
print('Sua parede tem dimensão de ', h,'x',l,' e a sua area é de ', a,'m²')
print('Para pintar essa parede é necessário {}l de tinta'.format(lit))
