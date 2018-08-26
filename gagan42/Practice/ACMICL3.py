t=int(input())
for i in range(t):
  n=int(input())
  l=[]
  for j in range(n):
    l.append(input())
  d=[]
  c=0
  for j in l:
    if j not in d:
      d.append(j)
      if(l.count(j)%2!=0):
        c=c+1
  print(c)
