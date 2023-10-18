print('Faça a simulação da prestação de sua casa aqui!')
nome = str(input('Informe o seu nome: '))
v = float(input('Insira o valor da casa que deseja comprar: R$ '))
a = int(input('Em quantos anos você pretende pagar :'))
s = float(input('Informe o seu salário atual: '))
p = v / (a*12)
if p <= s * 0.3:
    print('\033[1;0;42mParabéns!\033[0m, {}, você poderá adquirir sua casa por '.format(nome), a*12,' paarcelas de R${:.2f}'.format(p))
else:
    print('\033[1;0;41mLamento\033[0m, a parcela da casa excede 30% do seu salário.\n seu empréstimo foi negado!')
