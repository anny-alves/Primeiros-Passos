dados = dict()
situação = ' '
dados['aluno'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados["aluno"]}: '))
if dados['média'] >= 7:
    situação = 'Aprovado'
else:
    situação = 'Reprovado'
dados['situação'] = situação
for k, v in dados.items():
    print(f'{k} é igual a {v}')
