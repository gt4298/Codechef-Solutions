t=int(input())
for _ in range(t):
  n=int(input())
  l=list(map(int,input().split()))
  f=0
  k=[]
  for i in range(len(l)):
    f=f^(l[i]+l[i])
  print(f)
