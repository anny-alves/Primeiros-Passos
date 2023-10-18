print("{:=^40}".format("Conversor de medidas"))
medida = float(input("Insira a medida desejada em metro"))
cm = medida*100
mm = medida*1000
print("Convertendo {} temos {:.2f}cm e {:.2f}mm".format(medida, cm, mm))
