a,b=map(int,input().split())
e=[]
q=[]
s=[]
for i in range(1,a*a):
    e.append(a*i)
for j in range(1,b*b):
    s.append(b*j)
for k in e:
    if k in s:
        q.append(k)
print(min(q))