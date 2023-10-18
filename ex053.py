# detector de palidromo #
frase = str(input('Digite sua frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(inverso)
'''for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(inverso)'''
if inverso == junto:
    print(' A frase é um palidromo.')
else:
    print(' A frase não é um plidromo.')

