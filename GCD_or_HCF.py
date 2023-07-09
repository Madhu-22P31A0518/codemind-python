a,b=map(int,input().split())
e=[]
q=[]
s=[]
for i in range(1,a+1):
    if a%i==0:
        e.append(i)
for j in range(1,b+1):
    if b%j==0:
        q.append(j)
for k in e:
    if k in q:
        s.append(k)
print(max(s))