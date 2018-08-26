t=int(input())
from collections import Counter
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    z=dict(Counter(l))
    print(sum(z.values())-len(set(l)))
