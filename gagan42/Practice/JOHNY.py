t=int(input())
for _ in range(t):
  n=int(input())
  l=list(map(int,input().split()))
  k=int(input())
  m=l[k-1]
  l.sort()
  k=l.index(m)
  print(k+1)
