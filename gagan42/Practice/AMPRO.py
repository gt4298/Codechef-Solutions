m=input().split()
l=".".join([i[0].upper() for i in m[0:len(m)-1]])+"."+m[len(m)-1].title()
print(l)
