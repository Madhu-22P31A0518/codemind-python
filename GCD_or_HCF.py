a,b=map(int,input().split())
e=[]
q=[]
c=[]
for i in range(1,b*b):
    if a%i==0:
        e.append(i)
    if b%i==0:
        c.append(i)
for j in e:
    if j in c:
        q.append(j)
print(max(q))