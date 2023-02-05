import math
import itertools




def circulo (X):
    x = [float(x) for x in X.split()]
    ncirculos = int(x[0])

    def permutacoes_primeira_posicao(vetor):
        resultado = []
        for permutacao in itertools.permutations(vetor[1:]):
            resultado.append((vetor[ncirculos],) + permutacao)
        return resultado
    i = 1
    total = x[1] + x[ncirculos]
    base = 0
    baseant = 0
    maior = 0


def circulo (X):
    x = [float(x) for x in X.split()]
    ncirculos = int(x[0])
    i = 1
    total = x[1] + x[ncirculos]
    base = 0
    baseant = 0
    maior = 0

    #while ncirculos > 0:
    #    if i >= ncirculos:
    #        break
    #    if x[i] >= x[i+1] and x[i] > maior:
    #        maior = x[i]
    #    i += 1


    #    distanciaminima = maior * math.sqrt(2 - 2 * math.cos(360 / ncirculos))
    #    largura = (maior + distanciaminima) * math.sqrt(ncirculos / math.pi)


    #ncirculos = int(x[0]) 
    #i = 1  
    #print(distanciaminima)
    #print(largura)



    while ncirculos > 0:
        if i >= ncirculos:
            break

        circulo1 = x[i]
        circulo2 = x[i+1]

        hipotenusa = (circulo1 + circulo2)
        altura = abs(circulo1 - circulo2)

        h = hipotenusa*hipotenusa
        a = altura*altura
        base = math.sqrt(h - a)

        if i + 2 < len(x):
            circulo3 = x[i+2]
            hipotenusapos = (circulo3 + circulo2)
            alturapos = abs(circulo3 - circulo2)
            hpos = hipotenusapos*hipotenusapos
            apos = alturapos*alturapos
            baseant = base
            base = math.sqrt(hpos - apos)

            if (circulo3 + circulo1) > (base + baseant):
                hipotenusa = (circulo3 + circulo1)
                altura = abs(circulo3 - circulo1)
                h = hipotenusa*hipotenusa
                a = altura*altura
                total -= baseant

        base = math.sqrt(h - a)
        baseant = base
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