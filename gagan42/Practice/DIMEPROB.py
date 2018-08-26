t=int(input())
for _ in range(t):
    n=int(input())
    d1=n-90
    d2=n+90
    f=[]
    p=0
    for i in range(d1,d2+1):
        k=sum([int(x) for x in str(i)])
        k=k+i
        if(k==n):
            p=1
            f.append(i)
    if(p!=0):
        print(min(f))
    else:
        print("NONE")
