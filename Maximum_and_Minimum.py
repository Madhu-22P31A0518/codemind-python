n=int(input())
a=list(map(int,input().split()))
e=[]
c=0
for i in a:
    if a.count(i)==i:
        e.append(i)
        c+=1
if c==0:
    print('-1')
else:
    d=set(e)
    f=max(d)
    x=min(d)
    print(x,f,end=' ') 