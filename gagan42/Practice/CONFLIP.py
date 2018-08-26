t=int(input())
for _ in range(t):
  g=int(input())
  for _ in range(g):
    i,n,q=map(int,input().split())
    if(n%2!=0):
      if(i==1):
        tail=n//2+1
        head=n//2
      if(i==2):
        tail=n//2
        head=n//2+1
    else:
      tail,head=n//2,n//2
    if(q==1):
      print(head)
    else:
      print(tail)
