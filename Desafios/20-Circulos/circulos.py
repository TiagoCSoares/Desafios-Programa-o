import math

def circulo (X):
    x = [float(x) for x in X.split()]
    ncirculos = int(x[0])
    i = 1
    total = x[1] + x[ncirculos]
    base = 0

    while ncirculos > 0:
        if i >= ncirculos:
            break
        circulo1 = x[i]
        circulo2= x[i+1]

        hipotenusa = (circulo1 + circulo2)
        altura = abs(circulo1 - circulo2)

        h = hipotenusa*hipotenusa
        a = altura*altura

        base = math.sqrt(h - a)

        total += base
        i += 1

    return total
    
n = input()
n = int(n)

def main():
    while (n > 0):
        try:
            X = input()
            result = circulo(X)
            print("{:.3f}".format(result))
        except EOFError:
            break
main()