import numpy as np

X = input()
X = [int(X) for X in X.split()]



largura = X[0]
altura = X[1]
matriz = np.ones((altura, largura), dtype=int)
print(matriz)