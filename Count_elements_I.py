a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
q=set(c)
f=set(d)
v=0
for i in q:
    if i in f:
        v+=1
print(v)