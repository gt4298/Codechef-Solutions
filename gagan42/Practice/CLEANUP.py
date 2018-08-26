t=int(input())
for _ in range(t):
  n,m=map(int,input().split())
  l=list(map(int,input().split()))
  k=[x for x in range(1,n+1) if x not in l]
  c=[]
  a=[]
  for x in range(len(k)):
    if(x%2==0):
      c.append(k[x])
    else:
      a.append(k[x])
  print(*c)
  print(*a)
