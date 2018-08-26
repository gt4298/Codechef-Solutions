t=int(input())
for i in range(t):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l3=l2[::-1]
    op=lambda x,y:x<=y
    l=[op(l1[x],l2[x]) for x in range(n)]
    k=[op(l1[x],l3[x]) for x in range(n)]
    c1=l.count(True)
    c2=k.count(True)
    if(c1==n and c2!=n):
        print("front")
    elif(c1!=n and c2==n):
        print("back")
    elif(c1==n and c2==n):
        print("both")
    else:
        print("none")
