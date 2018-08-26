n,k=map(int,input().split())
s=[int(x) for x in input().split()]
l=[]
temp=0
flag=0
for i in range(0,len(s)-1):
	if(s[i]<0):
		s[i]=-s[i]
		s[i+1]=-s[i+1]
		temp=temp+1
		l.append(i+1)
if(s[-1]<0):
	temp=temp+1
	l.append(n)
print(temp)
for i in range(0,len(l)):
	print(l[i],end=" ")
