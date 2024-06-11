#ENTRADA
l,c=map(int, input().split())
matriz=[]
for i in range(l):    
    linha=list(map(int, input().split()))
    matriz.append(linha)

x,y=0,0
for a in range(1,l):
    for b in range(1,c):
        if matriz[a][b]==42:
            if matriz[a-1][b-1]==7 and matriz[a-1][b]==7 and matriz[a-1][b+1]==7 and matriz[a][b-1]==7 and  matriz[a][b+1]==7 and matriz[a+1][b-1]==7 and matriz[a+1][b]==7 and matriz[a+1][b+1]==7:
                x=a+1
                y=b+1
            
print(x,y)