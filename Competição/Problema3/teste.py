def chapeus(matriz):
    simbolos = sorted(set(simbolo for linha in matriz for simbolo in linha))
    
    for j in colunas:
        for i in linhas:
            simbolo = matriz[i][j]
            print(simbolo)
    return 0


n = input()
quantidades = [int(n) for n in n.split()]
linhas = quantidades[0]
colunas = quantidades[1]
turmas = quantidades[2]
def main():
    matriz = []
    for i in range(linhas):
        matriz.append(list(input().strip()))
    
    result = chapeus(matriz)
    print(result)

main()