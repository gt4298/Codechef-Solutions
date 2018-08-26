import math
t=int(input())
for i in range(t):
    a1,b1,n1 = input().split()
    a=int(a1)
    b=int(b1)
    n=int(n1)
    m=1000000007
    if n<=10:
        x=((a**n)%m)+((b**n)%m)
        y=abs(a-b)
        z=math.gcd( x, y )
        print (z)
    else:
        
        if a==b:
            print((pow(a,n,m)+pow(b,n,m))%m)
        else:
            x=(pow(a,n,abs(a-b))+pow(b,n,abs(a-b)))%abs(a-b)
            y=abs(a-b)
            z=(math.gcd(x,y))%abs(a-b)
            print(z)
