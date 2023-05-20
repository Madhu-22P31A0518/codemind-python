n=int(input())
a=list(map(int,input().split()))
b=[]
q=[]
for i in a:
    d=abs(i)
    b.append(d)
e=sorted(b)
for j in e:
    f=j*j
    q.append(f)
for k in q:
    print(k,end=' ')
    