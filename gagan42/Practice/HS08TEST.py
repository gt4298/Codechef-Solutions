x,y=map(float,input().split())
if(x%5==0 and y>=x+0.5):
    print(y-x-0.5)
elif(x%5==0 and y<x+0.5 or x%5!=0):
    print(y)
