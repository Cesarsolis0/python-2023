# Se tiene una matriz A, donde la matriz inversa de A se representa como A−1
# la cual
# es una matriz cuadrada que hace que la multiplicacion´ A × A−1
# sea igual a la matriz
# identidad I. Realizar un algoritmo que compruebe la siguiente propiedad:
# A × A−1 = I, donde I es la Matriz Identidad
import sys
A=[[10,10,0],[0,8,0],[5,0,4]]
print(f"la matriz A es:\n{A}")
#obtenemos la inversa de la matriz creada anteriormente
def inversa(A):
    #obtenemos el determinante de la matriz
    proceso = (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0]) + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))
    # si el determinante es 0 la matriz no es invertible por lo tanto el programa se cerrara
    if proceso == 0:
        print("La matriz A no es invertible.")
        sys.exit()
    #si el determinante es distinto de 0 ,continuamos buscando la matriz de cofactores
    else:
        cofactores = [[A[1][1] * A[2][2] - A[1][2] * A[2][1],-(A[1][0] * A[2][2] - A[1][2] * A[2][0]),A[1][0] * A[2][1] - A[1][1] * A[2][0]],
                   [-(A[0][1] * A[2][2] - A[0][2] * A[2][1]),A[0][0] * A[2][2] - A[0][2] * A[2][0],-(A[0][0] * A[2][1] - A[0][1] * A[2][0])],
                   [A[0][1] * A[1][2] - A[0][2] * A[1][1],-(A[0][0] * A[1][2] - A[0][2] * A[1][0]),A[0][0] * A[1][1] - A[0][1] * A[1][0]]]
    #luego buscamos la matriz adjunta              
        adjunta=[]
        for i in range(len(A)):
            filas=[]
            for j in range(len(A[0])):
                filas.append(cofactores[i][j])
            adjunta.append(filas)
    #finalmente obtenemos la inversa dibidiendo la matriz adjunta entre el determinante
        inversa = []
        for i in range(len(A)):
            fila=[]
            for j in range(len(A[0])):
                fila.append(adjunta[j][i]/proceso)
            inversa.append(fila)
        return inversa
# asignamos la matriz inversa a una variable y la imprimimos en pantalla      
A1=inversa(A)
print(f"la inversa de a es:\n{A1}")
# realizamos la multiplicacion de la matriz A y su inversa
def multiplicar(A,A1):
    if len(A[0]) != len(A1):
        print("No se pueden multiplicar las matrices. Las dimensiones no son válidas.")
        sys.exit()

    resultado=[]
    for i in range(len(A)):
        fila=[]
        for j in range(len(A1[0])):
            suma=0
            for k in range(len(A1)):
                suma = suma + A[i][k] * A1[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado
# asignamos el resulatdo a una variable e imprimimos en pantalla
AxA1=multiplicar(A,A1)
print(f"el resultado de la multiplicacion es:\n{AxA1}")
# creamos la matriz identidad para realizar la compararcion
I=[[1,0,0],[0,1,0],[0,0,1]]
print(f"la matriz identidad es:\n{I}")
# si el resultado de la multiplicacion es igual a la matriz identidad la propiedad se cumple 
# y si son distintos no se cumple
if AxA1 == I :
    print("la propiedad se cumple")
else:
    print("la propiedad no se cumple")
