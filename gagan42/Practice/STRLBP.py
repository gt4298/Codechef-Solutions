t=int(input())
for _ in range(t):
  s=input()
  k=s.count("01")+s.count("10")
  if(k<=2):
    print("uniform")
  else:
    print("non-uniform")
