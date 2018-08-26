def coeff(n,k):
 
    if(k>n-k):
        k=n-k
        
    res=1
 
    for i in range(k):
        
        res=res*(n-i)
        res=res//(i+1)
        
    return res
 
def modulo(x,y,mod):
    
    res=1
    x=x%mod
 
    while(y>0):
 
        if(y&1==1):
            res=(res*x)%mod
 
        y=y>>1
        x=(x*x)%mod
 
    return res
 
t=int(input())
mod=10**9+7
var=lambda a,s,f:(f*s)//a
  
for _ in range(t):
    
    n,k=map(int,input().split())
    l=sorted(list(map(int,input().split())))
    a,s,d=n-1,n-k,k-1
    x=coeff(a,d)
    p=1
    f=x
 
    for i in range(1,n//2):
 
        y,z=0,0
        
        if(n-i-1>=k-1):
            
            a,s=n-i-1,n-i-k
            f=var(a+1,s+1,f)
            y=f
            
        if(i>=k-1):
            
            a,s=i,i-k+1
            z=coeff(a,d)
 
        g=(x-y-z)%(mod-1)
        p=((p%mod)*modulo(l[i],g,mod)*modulo(l[n-i-1],g,mod))%mod
 
    print(p)
