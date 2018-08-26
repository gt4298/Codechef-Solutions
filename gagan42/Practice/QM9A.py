import collections
t=int(input())
for iss in range(t):
    n=input()
    s=input().split()
    a=[]
    v=[]
    
            
 
 
    for i in s:
        if( 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i):
            a.append(i[::-1])
     
    for i in a:
        for j in i:
            if(j in 'aeiou'):
                v.append(j)
                break
    d=collections.Counter(v)        
    s=0
    for i in d.values():
        if(i>1):
            s=s+i
            
    print(s)
