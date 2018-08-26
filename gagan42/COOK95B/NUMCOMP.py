t=int(input())
for _ in range(t):
    a,b,n=map(int,input().split())
    aa,bb=map(abs,[a,b])
    if(n%2==0):
        if(aa>bb):
            print(1)
        elif(aa<bb):
            print(2)
        elif(aa==bb):
            print(0)
    if(n%2!=0):
        if(a>b):
            print(1)
        elif(a<b):
            print(2)
        elif(a==b):
            print(0)
