print(' ======== ANALISADOR DE TRIANGULOS ========')
print('===========================================')
a = float(input('Insira o primeio segmento: '))
b = float(input('Insira o segundo segmento: '))
c = float(input('Insira o terceiro segmento: '))
if a > abs(b - c) and b > abs(a - c) and c > abs(a - b):
    if a == b and b == c:
        print('Os seguimentos formam um triângulo Equilátero!')
    elif a == b or b == c or a == c:
        print('Os seguimentos formam um triângulo Isoceles!')
    else:
        print('Os seguimentos formam um triângulo Escaleno!')
else:
    print('Os segmentos não podem formar um triângulo!')

