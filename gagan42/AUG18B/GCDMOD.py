def gcd(a,b):
    if(a<b):
        a,b=b,a
    while(b>0):
        r=a%b
        a=b
        b=r
    return a
 
 
#from math import gcd
 
t=int(input())
mod=10**9+7
for _ in range(t):
    a,b,n=map(int,input().split())
    s1=abs(a-b)%mod
    a=pow(a,n,mod-1)
    b=pow(b,n,mod-1)
    s=a+b
    print(gcd(s,s1)%mod)
