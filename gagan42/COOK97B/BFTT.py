t=int(input())
for _ in range(t):
    n=int(input())
    c=str(n).count('3')
    x=n
    if(c>=3):
        x=n+1
    for i in range(x,x+1001):
        c=str(i).count('3')
        if(c>=3):
            print(i)
            break
