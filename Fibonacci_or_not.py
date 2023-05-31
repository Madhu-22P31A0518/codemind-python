n=int(input())
e=[]
d=[]
a=0
b=1
c=a+b
d.append(a)
d.append(b)
d.append(c)
for i in range(3,n+1):
    a=b
    b=c
    c=a+b
    e.append(c)
f=d+e
if n in f:
    print(True)
else:
    print(False)