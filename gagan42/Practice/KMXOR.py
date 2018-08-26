t=int(input())
for ijk in range(0,t):
    n,k=map(int,input().strip().split())
    bit=[]
    req=[]
    c=0
    length=0
    f=int(k)
    while k!=0:
        w=k%2
        length+=1
        bit.append(w)
        k=k//2
        if w==0:
            c+=1
            req.append(1)
        else:
            req.append(0)
    if c==0:
        if f>1:
            if n%2==0:
                if n==2:
                    print(f-1,1)
                else:
                    print(f,1,2,3,'1 '*(n-4))
            else:
                print(f,'1 '*(n-1))
        else:
            print('1 '*n)
    else:
        if n%2==0:
            num=0
            for i in range(0,length):
                if bit[i]==0:
                    num+=pow(2,i)
            print(f,num,'1 '*(n-2))
        else:
            if n==1:
                print(f)
            else:
                if c==1:
                    if f==2:
                        print(f,'1 '*(n-1))
                    else:
                        n1=n2=0
                        for i in range(0,length):
                            if bit[i]==0:
                                n1+=pow(2,i)
                                break
                        if i==0:
                            n2+=pow(2,i+1)
                            n1+=pow(2,i+1)
                        else:
                            
                            n2+=pow(2,i-1)
                            n1+=pow(2,i-1)
                        print(n1,n2,f,(n-3)*'1 ')
                        
                        
                        
                    
                    
 
                else:
                    y=0
                    n1=n2=0
                    for i in range(0,length):
                        if bit[i]==0:
                            if y==0:
                                n1+=pow(2,i)
                                y=1
                            else:
                                n2+=pow(2,i)
                                y=0
                    print(f,n1,n2,'1 '*(n-3))
