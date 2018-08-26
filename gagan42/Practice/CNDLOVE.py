t=int(input())
for _ in range(t):
  n=int(input())
  l=list(map(int,input().split()))
  n=sum(l)
  if((n-1)%2==0):
    print("YES")
  else:
    print("NO")
