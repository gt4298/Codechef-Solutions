rt = 0
 
for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3 = map(int, input().strip().split(' '))
    d1 = (x1 - x2)**2 + (y1 - y2)**2
    d2 = (x2 - x3)**2 + (y2 - y3)**2
    d3 = (x3 - x1)**2 + (y3 - y1)**2
    if d1 + d2 == d3 or d1 + d3 == d2 or d2 + d3 == d1:
        rt += 1
print(rt)
