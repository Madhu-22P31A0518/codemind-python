a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
q=set(c)
f=set(d)
n=0
for i in q:
    if i not in f:
        n+=1
for j in f:
    if j not in q:
        n+=1
print(n)