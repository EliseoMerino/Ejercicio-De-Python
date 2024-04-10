n1 = int (input("ingrese nota 1:"))
n2 = int (input("ingrese nota 2:"))
n3 = int (input("ingrese nota 3:"))
promedio = (n1+n2+n3)/3
if promedio >=7:
    print ("muy bueno")
else:
    if promedio>=4:
        print("regular")
    else:
        print("reprobado")