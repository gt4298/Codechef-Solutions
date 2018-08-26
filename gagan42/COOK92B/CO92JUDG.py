t=int(input())
for _ in range(t):
    n=int(input())
    alice=list(map(int,input().split()))
    bob=list(map(int,input().split()))
    a=sum(alice)-max(alice)
    b=sum(bob)-max(bob)
    if(a<b):
        print("Alice")
    elif(a>b):
        print("Bob")
    else:
        print("Draw")
