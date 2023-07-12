n=int(input())
a=list(map(int,input().split()))
d=sorted(a)
e=[]
q=[]
for i in d:
    for j in range(1,d[-1]):
        if i%j==0:
            e.append(j)
for j in e:
    if e.count(j)==n:
        q.append(j)
f=set(q)
s=sorted(f)
print(s[-1])