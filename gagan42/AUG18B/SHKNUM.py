import math
def power(n):
    p=int(math.log2(n))
    return 2**p
def nextpower(n):
 
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    n += 1
    return n
t=int(input())
for _ in range(t):
    n=int(input())
    
    if(n==1):
        print(2)
        continue
    
    if(n&(n-1)==0 and n!=1):
        print(1)
        continue
    k=int(power(n))
    p=n-k
    a=power(p)
    b=nextpower(p)
    if k==b:
        print(min(b-p+1,p-a))
    else:
        print(min(p-a,b-p))
