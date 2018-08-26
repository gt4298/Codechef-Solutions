t=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
m=max(l)
n=m
q=m
for i in range(len(k)):
    if(k[i]==1):
        if(l[i]<m):
            m=l[i]
    if(k[i]==2):
        if(l[i]<n):
            n=l[i]
    if(k[i]==3):
        if(l[i]<q):
            q=l[i]
print(min((m+n,q)))
