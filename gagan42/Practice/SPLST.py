t=int(input())
for _ in range(t):
    *l,x,y=map(int,input().split())
    a,b,c=l
    p=min(l)
    if(a+b+c==x+y):
        if(p>x or p>y):
            print("NO")
        else:
            print("YES")
    else:
        print("NO")
