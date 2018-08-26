t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for i in l:
        if(i%m==0):
            c=c+1
    print(2**c-1)
