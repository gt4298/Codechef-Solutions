t=int(input())
for i in range(t):
    c=0
    s=input()
    for j in range(len(s)-3):
        st="".join(sorted(s[j]+s[j+1]+s[j+2]+s[j+3]))
        if(st=="cefh"):
            c=c+1
    if(c>0):
        print("lovely",c)
    else:
        print("normal")
