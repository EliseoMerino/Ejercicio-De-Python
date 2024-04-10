lista = []
num = int(input("Digite un valor:(0 para finalizar)") )
while num !=0:
    lista.append(num)
    num=int(input("Digite otro valor (0 para finalizar)"))
    print (lista)
    print ("tañano de la lista:")
    print(len(lista))