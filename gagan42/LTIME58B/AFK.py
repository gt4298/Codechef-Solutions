t=int(input())
import math
for _ in range(t):
    a,b,c=list(map(int,input().split()))
    s=abs(2*b-(a+c))
    print(int(math.ceil(s/2)))
