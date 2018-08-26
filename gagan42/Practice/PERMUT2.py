n=int(input())
while(n!=0):
    l=list(map(int,input().split()))
    k=[0]*len(l)
    for i in range(len(l)):
        c=l[i]
        k[c-1]=i+1
    if(k==l):
        print("ambiguous")
    else:
        print("not ambiguous")
    n=int(input())
