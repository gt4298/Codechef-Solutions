n,q=map(int,input().split())
l=list(map(int,input().split()))
for _ in range(q):
    x,y=map(int,input().split())
    f=sorted(l[x-1:y])
    p=len(bin(f[len(f)-1]))-2
    k=[("0"*(p-len(bin(i)[2:]))+bin(i)[2:]) for i in f]
    p="1"*(31-len(k[0]))
    t=[]
    for j in range(len(k[0])):
        s=""
        for i in k:
            s=s+i[j]
        t.append(s.count("1")>=s.count("0"))
    for i in t:
        if(i==True):
            p=p+"0"
        else:
            p=p+"1"
    print(int(p,2))
