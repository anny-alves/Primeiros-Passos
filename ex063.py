#Sequência de fibonacci
print(' =-=-=-=-= Sequência de Fibonacci =-=-=-=-=')
n = int(input('Quantos números deseja ver? '))
c = 2
t1 = 0
t2 = 1
print('Os {} primeiros termos da sequência de Fioncci é:'.format(n))
if n == 1:
    print('{}'.format(t1))
elif n == 2:
    print('{} -> {}'.format(t1, t2))
else:
    print('{} -> {}'.format(t1, t2), end=' -> ')
while c < n:
    t3 = t1 + t2
    print('{}'.format(t3), end=' -> ')
    t1 = t2
    t2 = t3
    c += 1
print('Fim')