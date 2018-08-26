import sys
sys.setrecursionlimit(10**5)
def choc(i,j):
    if i>j:
        return 0
    if ch[i][j]==-1:
        ch[i][j]=max(l[i]*(n-(j-i))+choc(i+1,j),l[j]*(n-(j-i))+choc(i,j-1))
    return ch[i][j]
 
for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    ch = [[-1 for i in range(n)] for j in range(n)]
    print(choc(0,n-1))
