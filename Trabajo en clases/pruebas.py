def arreglo():

    nombres=[]
    rut=[]

    for i in range(5):

        nombre=input("Ingrese el nombre de la persona: ")
        ci=input("ingrese el rut de la persona: ")

        nombres.append(nombre)
        rut.append(ci)

    return nombres , rut

def orden(nombres,rut):
    nombres.sort()
    rut.sort()
    return nombres , rut

print(arreglo())
print(orden())








