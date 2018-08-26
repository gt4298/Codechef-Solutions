t=int(input())
for i in range(t):
    n=int(input())
    l=[]
    for j in range(n):
        l.append((tuple(map(int,input().split()))))
    loss=0
    for j in l:
        k=j[0]+(j[0]*j[2]/100)
        f=k-(k*j[2]/100)
        loss=loss+(j[1]*(j[0]-f))
    print(loss)
