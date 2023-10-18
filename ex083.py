exp = str(input('Digite uma expressão: '))
if exp.count('(') == exp.count(')'):
    print('Sua expressão é válida')
else:
    print('Sua expressão não é válida')
