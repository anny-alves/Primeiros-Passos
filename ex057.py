# digite o sexo correto #
s = str(input('SEXO [F/M]: ')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('Dados inválidos, informe seu sexo: ')).strip().upper()[0]
print('Você digitou um valor aceitável!')
