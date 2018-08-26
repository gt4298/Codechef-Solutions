t=int(input())
import math
for _ in range(t):
  n,m=map(int,input().split())
  print(2*math.gcd(n,m))
