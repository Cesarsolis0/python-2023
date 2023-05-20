# Aplicar el metodo de Gauss para invertir una matriz aleatoria de 3 a 5 de dimensi ´ on sin ´
# utilizar librerias. Imprimir la matriz original y luego la matriz inversa. Recordar que si una
# matriz A es una matriz cuadrada no-singular, es decir, tal que su determinante es distinto
# de cero se puede utilizar el Metodo de Eliminaci ´ on Gaussiana
import random

filas=int(random.randint(3,5))
columnas=int(random.randint(3,5))
def matriz(filas,columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            elemento=random.randint(1,9)
            matriz[i].append(elemento)
    return matriz
matriz1=matriz(filas,columnas)
print(f"la matriz creada es:\n{matriz1}")

def matrizidentidad(filas,columnas):
    identidad=[]
    for i in range(filas):
        identidad.append([])
        for j in range(columnas):
            if i == j:
                identidad[i].append(1)
            else:
                identidad[i].append(0)
    return identidad
midentidad=matrizidentidad(filas,columnas)
print(f"la matriz identidad es:\n{midentidad}")

def matrizinversa(matriz1):
    filas=len(matriz1)
    columnas=len(matriz1[0])
    minversa=[]
    for i in range(filas):
        minversa.append([])
        for j in range(columnas):
            minversa[i].append(0)
            for i in range(filas):
                minversa[i][j]+=matriz1[i][j]
                minversa[i][j]/=matriz1[i][i]
    return minversa
inversa=matrizinversa(matriz1)




