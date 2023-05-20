n=int(input())
a=list(map(int,input().split()))
e=[]
d=[]
for i in a:
    if i%2==0:
        e.append(i)
    else:
        d.append(i)
for j in e:
    print(j,end=' ')
for k in d:
    print(k,end=' ')