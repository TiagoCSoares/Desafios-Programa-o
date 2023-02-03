def encontrar(num):
    if num == 1:
        return (0,0)
    else:
        num -= 1
        B = 1
        ES = 1
        C = 1
        DS = 1
        DI =1
        A = 0

        i=0
        j=0
        while num > 0:
            for a in range(B):
                j+=1
                num-=1

                if(num == 0):
                    return (i,j)
            
            for a in range(A):
                i-=1
                j+=1
                num-=1

                if(num == 0):
                    return (i,j)
            
            for a in range(ES):
                i-=1
                num-=1

                if(num == 0):
                    return (i,j)

            for a in range(C):
                j-=1
                num-=1

                if(num == 0):
                    return (i,j)

            for a in range(DS):
                i+=1
                j-=1
                num-=1

                if(num == 0):
                    return (i,j)

            for a in range(DI):
                i+=1
                num-=1

                if(num == 0):
                    return (i,j)

            B += 1 
            ES += 1 
            C += 1 
            DS += 1 
            DI += 1 
            A += 1 







def main():
    while True:
        try:
            num = int(input())
            coord = encontrar(num)
            print(coord[0], coord[1])
        except EOFError:
            break
    
main()