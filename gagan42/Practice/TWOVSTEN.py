t=int(input())
for _ in range(t):
  x=int(input())
  if(x%5==0 and x%10!=0):
    print(1)
  elif(x%10==0):
    print(0)
  elif(x%5!=0 and x%10!=0):
    print(-1)
