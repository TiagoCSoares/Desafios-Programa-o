def lakaka(X, Z):
    listaX = [0]
    listaZ = [0]
    listaX.extend(list(X))
    listaZ.extend(list(Z))

    tamZ = len(Z)
    tamX = len(X)
    list0 = [1]*tamX

    for i in range(tamZ - 1):
        locals()["list" + str(i)] = [0]
        i += 1

    a = 1
    b = 1
    for a in range(tamZ - 1):
        for b in range(tamX - 1):
            if Z[a] == X[b]:
                locals()["list" + str(a)].append(locals()["list" + str(a-1)][] + )

        



        











def main():
    while True:
        try:
            X = input()
            Z = input()
            result = lakaka(X ,Z)
        except EOFError:
            break

main()