print("{:=^24}".format("Média Escolar"))
nome = str(input("Insira o nome do aluno"))
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1+n2)/2
print("A média escolar de {} é {:.2}".format(nome, m))
