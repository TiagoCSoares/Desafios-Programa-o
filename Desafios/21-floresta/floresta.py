import numpy as np

def retangulo(X):

    lakaka = []
    while True:
        arvore = input()   
        arvores = [int(arvores) for arvores in arvore.split()]
        teste = arvores[0]
        lakaka.append(arvores)
        if teste == 0:
            break
    return lakaka

def area(bluepen,X):
    largura = X[1]
    altura = X[0]
    matriz = np.ones((altura, largura), dtype=int)
    for i in range (len(bluepen)):
        j = 1
        testes = bluepen[i]
        if testes[0] == 0:
            break
        for j in range (len(bluepen)):
            matriz[bluepen[i][j]][bluepen[i][j+1]] = 0
                    
    return matriz



def main():
    n = input()
    n = int(n)
    while (n > 0):
        try:
            X = input()
            X = [int(X) for X in X.split()]
            bluepen = retangulo(X)
            testa = bluepen[0]
            if testa[0] == 0:
                result = X[0]*X[1]
                print(result)
            else:
                print(X)
                result = area(bluepen,X)
                print(result)

        except EOFError:
            break
main()