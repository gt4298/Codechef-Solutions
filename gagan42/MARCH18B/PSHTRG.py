n,q=map(int,input().split())
l=list(map(int,input().split()))
op=lambda x:[x[j] for j in range(len(x)-2) if(x[j]+x[j+1]>x[j+2])]
for i in range(q):
    v,x,y=map(int,input().split())
    if(n>=3):
        if(v==1):
            l[x-1]=y
        if(v==2 and v!=1):
            k=sorted(l[x-1:y])
            f=op(k)
            if(len(f)==0):
                print(0)
            else:
                m=max(f)
                ind=k.index(m)
                print(k[ind]+k[ind+1]+k[ind+2])
