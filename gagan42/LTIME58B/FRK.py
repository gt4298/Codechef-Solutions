from itertools import product
l=["ch","he","ef","che","hef","chef"]
t=int(input())
c=0
for _ in range(t):
    s=input()
    for i in l:
        if(i in s):
            c=c+1
            break
print(c)
