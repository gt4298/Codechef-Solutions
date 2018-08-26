t=int(input())
import math
#from bisect import *
for i in range(t):
    n,h=map(int,input().split())
    l=sorted(list(map(int,input().split())))
    #k=bisect(l,h,0,n)
    m=0
    for j in range(1,max(l)+1):
        f=sum([math.ceil(x/j)if (x>j) else 1 for x in l ])
        if(f<=h):
            m=j
            break
    print(m)
