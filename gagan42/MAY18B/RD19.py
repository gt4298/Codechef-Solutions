t=int(input())
from math import gcd
for _ in range(t):
  n=int(input())
  l=list(map(int,input().split()))
  g=l[0]
  for i in range(1,len(l)):
    g=gcd(g,l[i])
  if(g==1):
    print(0)
  else:
    print(-1)
