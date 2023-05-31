a,b=map(int,input().split())
d=str(a)
e=d[0:b]
f=d[-b:]
n=int(e)
m=int(f)
q=n-m
print(abs(q))