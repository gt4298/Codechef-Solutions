def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x            
n=int(input())
l=list(map(int,input().split()))
q=int(input())
for i in range(q):
    k=list(map(int,input().split()))
    if(k[0]==1):
        x,y=k[1],k[2]
        l[x-1]=y
    else:
        low,r,g=k[1],k[2],k[3]
        c=0
        for f in (l[low-1:r]):
            if(gcd(f,g)==1):
                c=c+1
        print(c)
