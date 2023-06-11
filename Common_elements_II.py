a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
f=c+d
e=[]
for i in f:
    if f.count(i)==1:
        e.append(i)
for j in e:
    print(j,end=' ')