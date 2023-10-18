#Tabuada 3.0
print('Maquina de Tabuadas')
while True:
    print('-'*45)
    n = int(input('Digite o número que deseja saber a tabuada: '))
    print('-'*45)
    if n>= 0:
        print(f'A tabuada de {n} é: ')
        for mult in range(1,11):
            print(f'{n} X {mult} = {n*mult}')
    else:
        break
print('Programa de tábuada encerrado')
