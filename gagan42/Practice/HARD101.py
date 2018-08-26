l = list(map(int,input().split()))
l.sort()
mid = len(l)//2
l[mid],l[mid-1] = l[mid-1],l[mid]
print(*l)
