nome = str(input('Digite seu nome completo: ')).strip()
print('Olá, muito prazer!')
separa = nome.split()
print('Seu primeiro nome é {}'.format(separa[0].title()))
print('E seu ultimo nome é {}'.format(separa[len(separa)-1].title()))