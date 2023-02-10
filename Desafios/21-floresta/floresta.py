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

def gera_matriz(bluepen,X):
    largura = X[1]
    altura = X[0]
    matriz = np.ones((altura, largura), dtype=int)
    a = 0
    for i in range (len(bluepen)):
        j = 1
        testes = bluepen[i]
        if testes[0] == 0:
            break
        for j in range (1,len(bluepen[i]),2):
            if j > len(bluepen[i]):
                break
            if j < 2:
                matriz[bluepen[i][j]][bluepen[i][j+1]] = 0 
            else:
                matriz[(bluepen[i][j] + bluepen[i][1])][(bluepen[i][j+1] + bluepen[i][2])] = 0   

    return matriz

def maior_retangulo(matriz,X):
    altura = X[0]
    largura = X[1]
    histograma = [0] * largura
    max_area = 0

    for i in range(altura):
        for j in range(largura):
            if i == 0 or j == 0 or matriz[i][j] == 0:
                histograma[j] = 0
            else:
                histograma[j] += 1
        
        stack = []
        histograma.append(0)
        for j in range(len(histograma)):
            while stack and histograma[stack[-1]] > histograma[j]:
                h = histograma[stack.pop()]
                w = j if not stack else j - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(j)
        
    for i in range(altura):
        for j in range(largura):
            if matriz[i][j] == 0:
                k = i
                while k < altura and matriz[k][j] == 0:
                    k += 1
                h = k - i
                k = j
                while k < largura and matriz[i][k] == 0:
                    k += 1
                w = k - j
                max_area = max(max_area, h * w)
    
    return max_area
    
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
                matriz = gera_matriz(bluepen,X)
                max_area = maior_retangulo(matriz,X)
                print(max_area)

        except EOFError:
            break
main()