n=int(input())
d=n*n
s=0
p=0
while n!=0:
    r=n%10
    n//=10
    s=s*10+r
e=s*s
while e!=0:
    f=e%10
    e//=10
    p=p*10+f
if d==p:
    print(True)
else:
    print(False)