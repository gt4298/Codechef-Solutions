s=input()
vow="aeiou"
con="bcdfghjklmnpqrstvwxyz"
p=1
k=""
    
for j in range(len(s)):
    
    if(j==0 and s[j]=='*'):
       p=p*21
       k='c'
    
    elif(s[j]=='*'):
        
        if(k=='v'):
            p=p*21
            k='c'            
        else:
            p=p*5
            k='v'
            
    else:
        k=s[j]
        
print(p)
