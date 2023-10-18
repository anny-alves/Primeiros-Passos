print('Calculo do IMC')
nome = str(input('Nome: '))
peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('{},você tem {:.2f} de IMC, você está ABAIXO DO PESO!'.format(nome, imc))
elif imc < 25:
    print('{},você tem {:.2f} de IMC, você está no PESO IDEAL!'.format(nome, imc))
elif imc < 30:
    print('{},você tem {:.2f} de IMC, você está com SOBREPESO!'.format(nome, imc))
elif imc < 40:
    print('{},você tem {:.2f} de IMC, você está com OBESIDADE!'.format(nome, imc))
else:
    print('{},você tem {:.2f} de IMC, você está com  OBESIDADE MÓRBIDA!'.format(nome, imc))
