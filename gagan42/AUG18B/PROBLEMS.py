def sort(sc,ns):
    for i in range(len(sc)):
        for j in range(len(sc)-i-1):
            if(sc[j]>sc[j+1]):
                sc[j],sc[j+1]=sc[j+1],sc[j]
                ns[j],ns[j+1]=ns[j+1],ns[j]
    return sc,ns
p,s=map(int, input().split())
l=[]
for i in range(p):
    sc,ns=list(map(int, input().split())),list(map(int, input().split()))
    sc,ns=sort(sc,ns)
    n=0
    for j in range(len(ns)-1):
        if(ns[j]>ns[j+1]):
            n+=1
    l.append((n,i+1))
l.sort()
for i in l:
    print(i[1])
