import math
for _ in range(int(input())):
  n=int(input())
  s=int(math.sqrt(n))
  k=n//s
  r=n%s
  p=n//k
  if r==0:
    print("X"*k+"D"*p)
  else:
    print("X"*r+"D"+"X"*(k-r)+"D"*p)
