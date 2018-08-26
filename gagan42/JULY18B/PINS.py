t=int(input())
from fractions import Fraction
for _ in range(t):
    
    n=int(input())
    if(n==1):
        print(1,1)
    else:
        
        if(n%2==0):
            m=n//2
            c=m-1
            
        else:
            m=(n-1)//2
            c=m
        k=n-1
        print(1,10**(k-c))
