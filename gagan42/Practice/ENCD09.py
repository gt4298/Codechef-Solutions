n=int(input())
while(n!=0):
    if(n%2==0):
        print((n*(n-2)*(2*n-5))//24)
    else:
        print(((n-1)*(n-3)*(2*n-1))//24)
    n=int(input())
