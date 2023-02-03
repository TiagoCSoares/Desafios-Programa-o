import math

def encontrar(sec):
    num = sec
    raiz = math.sqrt(num)
    passos = int(raiz)
    if sec == 1:
        return (1,1)
    if sec == 2:
        return (1,2)
    if sec == 3:
        return (2,2)
    if sec == 4:
        return (2,1)
    else:
        sec = sec - (passos ** 2)
        if sec == 0:
            if passos % 2 == 0:
                j = passos
                i = 1
            else:
                i = passos
                j = 1
        if sec == 0:
            return (i,j)
        if passos % 2 == 0:
            j = passos
            i = 1

            if sec == 0:
                return (i,j)
            
            j += 1
            sec -= 1
            if sec == 0:
                return( i ,j)

            while sec > 0:
                for a in range(passos):
                    i+=1
                    sec-=1
                    if sec ==0:
                        return (i,j)
                for b in range(passos):
                    j-=1
                    sec-=1
                    if sec == 0:
                        return (i,j)
                i+=1
                sec-=1
                if sec == 0:
                    return (i,j)
                passos+=1
                for a in range(passos):
                    j+=1
                    sec-=1
                    if sec == 0:
                        return (i,j)
                for b in range(passos):
                    i-=1
                    sec-=1
                    if sec == 0:
                        return (i,j)
                j+=1
                sec-=1
                if sec == 0:
                    return (i,j)
                passos+=1

        else:
            i = passos -1
            j = 1

            if sec == 0:
                return (i,j)

            i += 1
            sec -= 1
            if sec == 0:
                return( i ,j)

            while sec > 0:
                for a in range(passos):
                    j+=1
                    sec-=1
                    if sec == 0:
                        return (i,j)
                for b in range(passos):
                    i-=1
                    sec-=1
                    if sec == 0:
                        return (i,j)
                j+=1
                sec-=1
                if sec == 0:
                    return (i,j)
                passos+=1
                for a in range(passos):
                    i+=1
                    sec-=1
                    if sec ==0:
                        return (i,j)
                for b in range(passos):
                    j-=1
                    sec-=1
                    if sec == 0:
                        return (i,j)
                i+=1
                sec-=1
                if sec == 0:
                    return (i,j)
                passos+=1
            


def main():
    while True:
        sec = int(input())
        if sec == 0:
            return
        pos = encontrar(sec)
        print(pos[1], pos[0])
    
main()