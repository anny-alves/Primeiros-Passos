print(' ======== ANALISADOR DE TRIANGULOS ========')
print('===========================================')
a = float(input('Insira o primeio segmento: '))
b = float(input('Insira o segundo segmento: '))
c = float(input('Insira o terceiro segmento: '))
if a > abs(b - c) and b > abs(a - c) and c > abs(a - b):
    print('Os seguimentos podem formar um triângulo!')
else:
    print('Os segmentos não podem formar um triângulo!')
