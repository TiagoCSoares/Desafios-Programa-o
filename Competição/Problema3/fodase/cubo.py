n = int(input())
area = 100000

for altura in range(1, n + 1):
    for largura in range(1, n + 1):
        for profundidade in range(1, n + 1):
            if largura * altura * profundidade > n:
                break
            menor = 2 * (largura * altura + largura * profundidade + altura * profundidade)
            if menor < area and largura * altura * profundidade == n:
                area = menor

print(area)