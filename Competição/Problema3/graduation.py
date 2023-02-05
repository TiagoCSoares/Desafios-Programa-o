def chapeus(matriz):
    simbolos = sorted(set(simbolo for linha in matriz for simbolo in linha))
    jaapareceu = []
    verifica = []
    cores = 0
    lakaka = 1

    for j in range(colunas):
        for i in range(linhas):
            for a in range(len(simbolos)):
                if matriz[i][j] == simbolos[a]:
                    if simbolos[a] not in jaapareceu:
                        jaapareceu.append(simbolos[a])
                        verifica.append(simbolos[a])
                    if simbolos[a] in jaapareceu:
                        verifica[a] = lakaka
                    if simbolos[a] in jaapareceu and simbolos[a] not in verifica:
                        lakaka += 1
                    
    print(simbolos)
    print(jaapareceu)
    print(matriz)
    return len(jaapareceu)



n = input()
quantidades = [int(n) for n in n.split()]
linhas = quantidades[0]
colunas = quantidades[1]
turmas = quantidades[2]
lakaka = 1


matriz = []
def main():
    while (linhas > 0):
        try:
            X = input().strip()
            matriz.append(list(X))
        except EOFError:
            break
    result = chapeus(matriz)
    print(result)

main()

