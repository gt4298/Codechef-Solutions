t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    f=0
    for i in l:
        if(i>=x):
            f=1
            break
    if(f):
        print("YES")
    else:
        print("NO")
