arr=[]
t=int(input())
for i in range(0, t):
    p= input().split()
    n=int(p[0])
    k= int(p[1])
 
    p= [int(x) for x in input().split()]
    a= p[::2]
    b= p[1::2]
    a.sort()
    b.sort(reverse=True)
    A= sum(a)
    B= sum(b)
    for j in range(0, k):
        if(A<B):
            break
        A= A- a[-1] + b[-1]
        B= B- b[-1] + a[-1]
        a[-1], b[-1]= b[-1], a[-1]
        a.sort()
        b.sort(reverse= True)
    if(A<B):
        print("YES")
    else:
        print("NO")
