import numpy as np


listaX = [0]
listaZ = [0]
listaX.extend(list(X))
listaZ.extend(list(Z))
tamZ = len(Z) + 1
tamX = len(X) + 1

matrix = np.zeros((tamZ, tamX))

matrix[0] = [1 for i in range(tamX)]


for i in range(tamZ):
    for j in range(tamX):
        if listaZ[i] == listaX[j]:
            matrix[i][j] = matrix[i-1][j-1] + matrix[i][j-1]
        else:
            matrix[i][j] = matrix[i][j-1]
        j =+ 1
    i =+ 1


print(matrix)