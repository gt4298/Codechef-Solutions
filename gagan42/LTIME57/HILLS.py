t=int(input())
for i in range(t):
    n,u,d=map(int,input().split())
    l=list(map(int,input().split()))
    k=0
    i=0
    while(i<len(l)-1):
      if(l[i]==l[i+1]):
        i=i+1 
      elif(l[i]<l[i+1]):
        if(l[i+1]-l[i]<=u):
          i=i+1 
        else:
          break
      elif(l[i]>l[i+1]):
        if(l[i]-l[i+1]>d and k==0):
          k=1 
          i=i+1 
        elif(l[i]-l[i+1]<=d):
          i=i+1 
        else:
          break
    print(i+1)
