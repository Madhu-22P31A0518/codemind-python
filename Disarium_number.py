n=int(input())
d=str(n)
x=[]
s=0
for i in d:
    e=d.index(i)+1
    q=int(i)
    f=q**e
    x.append(f)
for j in x:
    s=s+j
if s==n:
    print(True)
else:
    print(False)