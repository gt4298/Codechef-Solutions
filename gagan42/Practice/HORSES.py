def difference(l, n):
    l = sorted(l)
    diff =l[len(l)-1]-l[0]
 
    for i in range(n-1):
        if l[i+1] - l[i] < diff:
            diff = l[i+1]-l[i]
 
    return diff
t=int(input())
for _ in range(t):
  n=int(input())
  l=list(map(int,input().split()))
  print(difference(l,len(l)))
