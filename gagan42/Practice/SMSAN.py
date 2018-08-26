from fractions import Fraction
m=input().split()
l=[True for x in m if x in ["love","babe","sweety","life"]]
k=Fraction(l.count(True),len(m))
print(k.numerator,"/",k.denominator,sep="")
