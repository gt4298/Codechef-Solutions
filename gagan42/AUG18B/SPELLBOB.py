t=int(input())
for _ in range(t):
    f=input()
    r=input()
    k=f+r
    l=[(0, 1, 2), (0, 1, 5), (0, 2, 4), (0, 4, 5), (1, 2, 3), (1, 3, 5), (2, 3, 4),(3, 4, 5)]
    s=["bob","obb","bbo"]
    b=False
    for i in l:
        g=k[i[0]]+k[i[1]]+k[i[2]]
        if(g in s):
            b=True
            break
    if(b==True):
        print("yes")
    else:
        print("no")
