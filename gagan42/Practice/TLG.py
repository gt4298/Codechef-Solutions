t=int(input())
l=[0,0]
c1,c2=0,0
for _ in range(t):
  f=tuple(map(int,input().split()))
  c1+=f[0]
  c2+=f[1]
  if(c1>c2):
    if(c1-c2>l[1]):
      l=[1,c1-c2]
  else:
    if(c2-c1>l[1]):
      l=[2,c2-c1]
print(*l)
