#ler um numero de 0 a 20 e escrever por extenso com tuplas
n = ('zero','um', 'dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','desesseis','dezessete','dezoito','dezenove','vinte')
num = int(input('Digite um número entre 0 e 20: '))
while num < 0 or num > 20:
    num = int(input('Tente novemente.\n Digite um número entre 0 e 20: '))
print(f'Você digitou o número {n[num]}')
