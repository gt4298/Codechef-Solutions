from fractions import Fraction as frac
t=int(input())
for _ in range(t):
    n,a,k=map(int,input().split())
    s=(n-2)*180
    p=((2*s)/n)-(2*a)
    d=p/(n-1)
    x=a+((k-1)*d)
    f=frac(x).limit_denominator()
    print(f.numerator,f.denominator)
