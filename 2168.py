#ENTRADA

n=int(input())

matriz=[]

for i in range(n+1):
    linha=list(map(int,input().split()))
    matriz.append(linha)


#RESOLUÇÃO
for i in range(n):
    
    resposta_linha=[]
    
    for j in range(n):
        soma=0
        for l in range(2):
            for c in range(2):
                soma+=matriz[l+i][c+j]
    
        if soma>=2:
            resposta_linha.append("S")
        else:
            resposta_linha.append("U")
    
    print(*resposta_linha, sep="")


