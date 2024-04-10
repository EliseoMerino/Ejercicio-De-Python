sueldos = []
suma = 0 
for x in range (5):
    valor=float(input("ingrese sueldo operario:"))
    sueldos.append(valor)
    suma=suma+valor
print ("lista sueldos")
print (sueldos)
promedio=suma/5
print("promedio sueldos")
print(promedio)