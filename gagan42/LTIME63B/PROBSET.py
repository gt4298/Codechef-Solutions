test=int(input())
for _ in range(test):
    n,m=map(int,input().split())
    cases=[input().split() for _ in range(n)]
    weak=False
    invalid=False
    for index in cases:
        if(index[0]=='correct' and '0' in index[1]):
            invalid=True
            break
        elif(index[0]=='wrong' and '0' not in index[1]):
            weak=True
    if(invalid):
        print("INVALID")
    elif(weak):
        print("WEAK")
    else:
        print("FINE")
        
        
