from sys import stdin
t=int(stdin.readline())
for _ in range(t):
    n=int(stdin.readline())
    l=list(map(int,stdin.readline().split()))
    l.sort()
    m=9999999999999999
    for i in range(n-1):
        d=abs(l[i+1]-l[i])
        if(d<m):
            m=d
    print(m)
