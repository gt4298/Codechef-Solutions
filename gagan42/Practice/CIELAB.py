a,b=map(int,input().split())
s=a-b
if(s%10==9):
  print(s-1)
else:
  print(s+1)
