t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    p=sum(l)
    for i in l:
        s=p-i
        if(i+k>s):
            c=c+1
    print(c)
