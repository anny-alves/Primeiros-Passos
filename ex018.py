import math
ângulo = float(input('Digite o valor do ângulo: '))
s = math.sin(math.radians(ângulo))
c = math.cos(math.radians(ângulo))
t = math.tan(math.radians(ângulo))
print('Para o ângulo de {}° temos os valores de \n SENO={:.2f} \n COSSENO={:.2f} \n TANGENTE={:.2f} '.format(ângulo, s, c, t))
