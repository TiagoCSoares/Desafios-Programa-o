import math

def circulo (X):
    i = 0
    a, b, c = map(float, X.split())
    if a <= 0 or b <= 0 or c <= 0:
        raio = 0
        return raio
    if a + b <= c or a + c <= b or b + c <= a:
        raio = 0
        return raio 
    semiperimetro = (a + b + c) / 2
    areatrinagulo = math.sqrt(semiperimetro*(semiperimetro - a)*(semiperimetro - b)*(semiperimetro - c))
    raio = areatrinagulo / semiperimetro
    return raio

def main():
    while True:
        try:
            X = input()
            result = circulo(X)
            print('The radius of the round table is: '"{:.3f}".format(result))
        except EOFError:
            break

main()